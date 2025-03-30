from pyiceberg.catalog import load_catalog
from pyiceberg.table import Table
from pyiceberg.data import Record
from pyiceberg.types import TimestampType, StringType
from datetime import datetime

# Initialize Iceberg catalog and table
catalog = load_catalog("default")
table = catalog.load_table("my_namespace.my_table")

def process_and_store_message(message, topic, partition, offset):
    global current_window_start, current_window_data

    current_time = datetime.now()

    # Calculate the start of the current 5-minute window
    window_start = current_time - timedelta(
        minutes=current_time.minute % 5,
        seconds=current_time.second,
        microseconds=current_time.microsecond,
    )

    # If the window has changed, write the data to Iceberg
    if window_start != current_window_start:
        if current_window_data:
            write_to_iceberg(current_window_start, current_window_data)
            current_window_data = []  # Reset the data buffer
        current_window_start = window_start

    # Add the message to the current window's data
    current_window_data.append({"timestamp": current_time, "message": message})


def write_to_iceberg(window_start, data):
    # Convert data to Iceberg records
    records = [
        Record(timestamp=msg["timestamp"], message=msg["message"])
        for msg in data
    ]

    # Write records to Iceberg table
    table.append(records)
    logger.info(f"Wrote {len(records)} records to Iceberg table.")


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
        # Write any remaining data before exiting
        if current_window_data:
            write_to_iceberg(current_window_start, current_window_data)
        consumer.close()
        logger.info("Kafka consumer closed.")