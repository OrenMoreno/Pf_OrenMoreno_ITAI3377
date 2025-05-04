import asyncio
import random
import json
import time
from aiocoap import *

async def simulate_sensor_data():
    """Continuously generate and send simulated sensor data using CoAP"""
    # Create CoAP client context
    protocol = await Context.create_client_context()
    
    print("CoAP sensor simulation started")
    while True:
        try:
            # Generate random temperature and humidity values
            temperature = round(random.uniform(20.0, 25.0), 2)
            humidity = round(random.uniform(30.0, 50.0), 2)
            
            # Create a JSON payload
            data = {
                "temperature": temperature, 
                "humidity": humidity,
                "timestamp": time.time(),
                "sensor_id": "COAP-SENSOR-001"
            }
            
            payload = json.dumps(data).encode('utf-8')
            
            # Create CoAP POST request
            request = Message(code=POST, payload=payload)
            request.set_request_uri('coap://localhost/sensor/data')
            
            # Send request and await response
            response = await protocol.request(request).response
            
            print(f"CoAP Result: {response.code}")
            print(f"Sent: {data}")
            
            await asyncio.sleep(1)
        except Exception as e:
            print(f"CoAP error: {e}")
            await asyncio.sleep(5)  # Wait a bit longer if there's an error

if __name__ == "__main__":
    # Run the CoAP sensor simulation
    asyncio.run(simulate_sensor_data())
