from kafka import KafkaProducer
import pandas as pd
import json
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    api_version=(2, 8, 1),
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

df = pd.read_csv('employees.csv')

print(df.columns)

for _, row in df.iterrows():

    data = {
        "employee": row.iloc[0],
        "sales": int(row.iloc[1])
    }

    producer.send('etl_topic', value=data)

    print(f"Sent: {data}")

    time.sleep(2)

producer.flush()