import random
import time
import json
from kafka import KafkaProducer

# Set up Kafka producer
producer = KafkaProducer(bootstrap_servers=["localhost:29092"])

# Define a list of possible sensor ids
sensors = [
    "7a5d49ae-d49b-47a5-9fbb-153c964165bd",
    "312883eb-4682-4e65-813a-2e1a99954144",
    "15e14fa6-fcee-4afc-94f2-de3c84d9aa95",
    "1d6af219-4cc3-48fa-81ba-1d4923a13df9",
    "a3e94207-de9e-414e-a0d2-0a392aecfed7"
]

# Generate and send random sensor data to Kafka
while True:
    temperature = round(random.uniform(20, 30), 2)
    humidity = round(random.uniform(0, 100), 2)
    pressure = round(random.uniform(950, 1050), 2)

    # Select a random location from the list
    sensor = random.choice(sensors)

    # Add the location to the sensor data
    data = {
        "temperature": temperature,
        "humidity": humidity,
        "pressure": pressure,
        "sensor": sensor
    }

    producer.send(
        "sensor-data",
        json.dumps(data).encode('utf-8'),
        data["sensor"].encode('utf-8')
    )

    print("Sent: {}".format(data))

    # Sleep for 0.5 seconds before sending the next message
    time.sleep(0.5)
