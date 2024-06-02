from confluent_kafka import Consumer, KafkaError
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroDeserializer

# Schema Registry configuration
schema_registry_conf = {'url': 'http://130.61.209.12:8081'}
schema_registry_client = SchemaRegistryClient(schema_registry_conf)

# Avro deserializer
avro_deserializer = AvroDeserializer(schema_registry_client)

# Kafka consumer configuration
consumer_config = {
    'bootstrap.servers': '130.61.209.12:9092',
    'group.id': 'my-consumer-group2',
    'auto.offset.reset': 'earliest'
}

# Create Consumer instance
consumer = Consumer(consumer_config)

# Subscribe to the topic
consumer.subscribe(['CUSTOMER_TRANSACTIONS_TOTAL2'])

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(msg.error())
                break
        try:
            value = avro_deserializer(msg.value(), None)
            print(f"Received message: {value}")
        except Exception as e:
            print(f"Message deserialization failed: {e}")
except KeyboardInterrupt:
    pass
finally:
    consumer.close()