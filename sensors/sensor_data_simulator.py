# sensors/sensor_data_simulator.py
import time
import random
from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_sensor_data():
    while True:
        data = {
            "temperature": round(random.uniform(20, 100), 2),
            "vibration": round(random.uniform(0, 5), 2),
            "pressure": round(random.uniform(100, 200), 2)
        }
        producer.send('sensor_data', data)
        print(f"Sent data: {data}")
        time.sleep(2)

if __name__ == "__main__":
    generate_sensor_data()
