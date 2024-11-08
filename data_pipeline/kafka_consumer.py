# data_pipeline/kafka_consumer.py
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('sensor_data', bootstrap_servers='localhost:9092', value_deserializer=lambda m: json.loads(m.decode('utf-8')))

for message in consumer:
    data = message.value
    print(f"Received data: {data}")
    # Here you could add data processing code (cleaning, transformation, etc.)

