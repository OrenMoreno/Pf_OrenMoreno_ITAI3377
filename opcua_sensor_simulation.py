from asyncua import ua, Server
import asyncio
import random
import time

async def main():
    # Initialize OPC UA server
    server = Server()
    await server.init()
    
    # Set up server endpoint
    server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")
    
    # Set up server namespace
    uri = "http://examples.freeopcua.github.io"
    idx = await server.register_namespace(uri)
    
    # Get Objects node
    objects = server.nodes.objects
    
    # Create a custom object to hold our variables
    myobj = await objects.add_object(idx, "IIoTSensor")
    
    # Add variables to our custom object
    temperature = await myobj.add_variable(idx, "Temperature", 0.0)
    humidity = await myobj.add_variable(idx, "Humidity", 0.0)
    timestamp = await myobj.add_variable(idx, "Timestamp", 0.0)
    sensor_id = await myobj.add_variable(idx, "SensorID", "OPCUA-SENSOR-001")
    
    # Set variables to be writable
    await temperature.set_writable()
    await humidity.set_writable()
    await timestamp.set_writable()
    
    print("OPC UA Server started at opc.tcp://0.0.0.0:4840/freeopcua/server/")
    
    # Start the server and run the main loop
    async with server:
        while True:
            # Generate random temperature and humidity values
            temp_value = round(random.uniform(20.0, 25.0), 2)
            hum_value = round(random.uniform(30.0, 50.0), 2)
            current_time = time.time()
            
            # Update variables with new values
            await temperature.write_value(temp_value)
            await humidity.write_value(hum_value)
            await timestamp.write_value(current_time)
            
            print(f"OPC UA Updated - Temperature: {temp_value}, Humidity: {hum_value}")
            
            # Wait 1 second before next update
            await asyncio.sleep(1)

if __name__ == "__main__":
    # Run the OPC UA server
    asyncio.run(main())