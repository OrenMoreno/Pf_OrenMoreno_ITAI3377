import paho.mqtt.client as mqtt
import random
import time
import json

# MQTT Broker configuration
broker = "localhost"
port = 1883
topic = "sensor/data"

def simulate_sensor_data():
    """Continuously generate and publish simulated sensor data"""
    while True:
        # Generate random temperature and humidity values
        temperature = round(random.uniform(20.0, 25.0), 2)
        humidity = round(random.uniform(30.0, 50.0), 2)
        
        # Create a JSON payload
        payload = json.dumps({
            "temperature": temperature,
            "humidity": humidity,
            "timestamp": time.time(),
            "sensor_id": "MQTT-SENSOR-001"
        })
        
        # Publish to MQTT topic
        client.publish(topic, payload)
        print(f"MQTT Published: {payload}")
        
        # Wait 1 second before next reading
        time.sleep(1)

# Create MQTT client and connect to broker
client = mqtt.Client()
try:
    client.connect(broker, port)
    print(f"Connected to MQTT broker at {broker}:{port}")
    simulate_sensor_data()
except Exception as e:
    print(f"Failed to connect to MQTT broker: {e}")