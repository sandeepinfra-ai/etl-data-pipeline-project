from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    api_version=(2, 8, 1),
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

data = [
    {"employee": "Sandeep", "sales": 5000},
    {"employee": "Rahul", "sales": 7000},
    {"employee": "Anjali", "sales": 6500}
]

for record in data:
    producer.send('etl_topic', value=record)
    print(f"Sent: {record}")
    time.sleep(2)

producer.flush()