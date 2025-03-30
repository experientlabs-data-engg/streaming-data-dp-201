from confluent_kafka import Consumer, KafkaError
import json
from datetime import datetime, timedelta
from minio import Minio
from minio.error import S3Error
import logging
from io import BytesIO


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration
MINIO_ENDPOINT = "minio:9000"  # MinIO server endpoint
MINIO_ACCESS_KEY = "minioadmin"  # MinIO access key
MINIO_SECRET_KEY = "minioadmin"  # MinIO secret key
MINIO_BUCKET = "kafka-messages"  # MinIO bucket name
OFFSET_FILE = "offsets.json"  # File to store offsets

# Kafka consumer configuration
consumer_conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my_consumer_group',
    'auto.offset.reset': 'earliest',  # Start reading from the beginning of the topic
    'enable.auto.commit': False,  # Disable auto-commit to manually manage offsets
}

# Initialize Kafka consumer
consumer = Consumer(consumer_conf)
consumer.subscribe(['websocket_s3d'])  # Replace 'websocket_s3d' with your Kafka topic

# Initialize MinIO client
try:
    minio_client = Minio(
        MINIO_ENDPOINT,
        access_key=MINIO_ACCESS_KEY,
        secret_key=MINIO_SECRET_KEY,
        secure=False,  # Set to True if using HTTPS
    )
    logger.info("MinIO client initialized successfully.")
except Exception as e:
    logger.error(f"Failed to initialize MinIO client: {e}")
    exit(1)

# Ensure MinIO bucket exists
try:
    if not minio_client.bucket_exists(MINIO_BUCKET):
        minio_client.make_bucket(MINIO_BUCKET)
        logger.info(f"Created MinIO bucket: {MINIO_BUCKET}")
except S3Error as e:
    logger.error(f"Error creating MinIO bucket: {e}")
    exit(1)

# Track the current 5-minute window
current_window_start = None
current_window_data = []


def get_last_offset(topic, partition):
    """Retrieve the last committed offset from the offset file in MinIO."""
    try:
        # Download the offset file from MinIO
        response = minio_client.get_object(MINIO_BUCKET, OFFSET_FILE)
        offsets = json.loads(response.read().decode('utf-8'))
        response.close()
        response.release_conn()
        return offsets.get(f"{topic}-{partition}")
    except S3Error as e:
        if e.code == "NoSuchKey":
            logger.info("Offset file not found. Starting from the beginning.")
            return None
        logger.error(f"Error retrieving offset file: {e}")
        return None


def save_offset(topic, partition, offset):
    """Save the committed offset to the offset file in MinIO."""
    try:
        # Download the existing offset file (if it exists)
        try:
            response = minio_client.get_object(MINIO_BUCKET, OFFSET_FILE)
            offsets = json.loads(response.read().decode('utf-8'))
            response.close()
            response.release_conn()
        except S3Error as e:
            if e.code == "NoSuchKey":
                offsets = {}  # Create a new offset file if it doesn't exist
            else:
                raise e

        # Update the offset for the topic-partition
        offsets[f"{topic}-{partition}"] = offset

        # Convert updated offsets to JSON bytes
        json_data = json.dumps(offsets).encode("utf-8")
        json_bytes = BytesIO(json_data)

        # Upload the updated offset file to MinIO
        minio_client.put_object(
            MINIO_BUCKET,
            OFFSET_FILE,
            json_bytes,
            len(json_data),  # Ensure correct byte length
            content_type="application/json",
        )
        logger.info(f"Saved offset: topic={topic}, partition={partition}, offset={offset}")
    except S3Error as e:
        logger.error(f"Error saving offset file: {e}")



def process_and_store_message(message, topic, partition, offset):
    global current_window_start, current_window_data

    current_time = datetime.now()

    # Calculate the start of the current 5-minute window
    window_start = current_time - timedelta(
        minutes=current_time.minute % 5,
        seconds=current_time.second,
        microseconds=current_time.microsecond,
    )

    # If the window has changed, upload the data to MinIO
    if window_start != current_window_start:
        if current_window_data:
            upload_to_minio(current_window_start, current_window_data)
            current_window_data = []  # Reset the data buffer
        current_window_start = window_start

    # Add the message to the current window's data
    current_window_data.append({"timestamp": current_time.isoformat(), "message": message})

    # Save the offset after processing the message
    save_offset(topic, partition, offset)


def upload_to_minio(window_start, data):
    # Generate a filename for the 5-minute window
    filename = f"{window_start.strftime('%Y/%m/%d/%H/%M')}.json"

    # Convert data to JSON
    json_data = json.dumps(data)

    # Convert string to file-like object
    json_bytes = BytesIO(json_data.encode("utf-8"))

    # Upload the data to MinIO
    try:
        minio_client.put_object(
            MINIO_BUCKET,
            filename,
            json_bytes,
            len(json_data.encode("utf-8")),  # Ensure correct byte length
            content_type="application/json",
        )
        logger.info(f"Uploaded to MinIO: {filename}")
    except S3Error as e:
        logger.error(f"Error uploading to MinIO: {e}")


def consume_message():
    try:
        while True:
            msg = consumer.poll(1.0)  # Adjust the timeout as needed
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    logger.info(f"Reached end of partition: {msg.partition()}")
                else:
                    logger.error(f"Error: {msg.error()}")
            else:
                # Retrieve the last committed offset for the topic-partition
                last_offset = get_last_offset(msg.topic(), msg.partition())
                if last_offset is not None and msg.offset() <= last_offset:
                    logger.info(f"Skipping already processed message: offset={msg.offset()}")
                    continue

                # Process and store the received message
                process_and_store_message(
                    msg.value().decode('utf-8'),
                    msg.topic(),
                    msg.partition(),
                    msg.offset(),
                )

    except KeyboardInterrupt:
        logger.info("Consumer interrupted by user.")
    finally:
        # Upload any remaining data before exiting
        if current_window_data:
            upload_to_minio(current_window_start, current_window_data)
        consumer.close()
        logger.info("Kafka consumer closed.")


if __name__ == '__main__':
    logger.info("Starting Kafka consumer...")
    consume_message()