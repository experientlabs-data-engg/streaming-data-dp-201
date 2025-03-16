from pyiceberg.catalog import load_catalog
from pyiceberg.schema import Schema
from pyiceberg.types import StringType, TimestampType

# Define the schema
schema = Schema(
    fields=[
        ("timestamp", TimestampType(), "Timestamp of the message"),
        ("message", StringType(), "The Kafka message"),
    ]
)

# Create the table
catalog = load_catalog("default")
catalog.create_table(
    identifier="my_namespace.my_table",
    schema=schema,
    partition_spec=["timestamp"],  # Partition by timestamp
)