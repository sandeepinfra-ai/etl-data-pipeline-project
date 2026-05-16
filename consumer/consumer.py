from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'etl_topic',
    bootstrap_servers='localhost:9092',
    api_version=(2, 8, 1),
    auto_offset_reset='earliest',
    group_id='etl-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Waiting for messages...")

for message in consumer:
    print(f"Received: {message.value}")