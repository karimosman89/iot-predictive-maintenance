# kafka_producer.py
import json
import time
from kafka import KafkaProducer
import random

# Load Kafka configuration
with open('configs/kafka_config.yaml', 'r') as f:
    kafka_config = yaml.safe_load(f)['kafka']

producer = KafkaProducer(
    bootstrap_servers=kafka_config['bootstrap_servers'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_and_send_data():
    while True:
        data = {
            "temperature": round(random.uniform(20, 100), 2),
            "vibration": round(random.uniform(0, 5), 2),
            "pressure": round(random.uniform(100, 200), 2),
            "timestamp": int(time.time())
        }
        producer.send(kafka_config['topic'], data)
        print(f"Sent data: {data}")
        time.sleep(2)

if __name__ == "__main__":
    generate_and_send_data()

