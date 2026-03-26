import asyncio
from bleak import BleakScanner, BleakClient

# These will be set to match the ESP32 code later
ESP32_NAME = "FITNESS_ESP32"
CHARACTERISTIC_UUID = "00002a37-0000-1000-8000-00805f9b34fb" 

async def scan_and_connect():
    print("Scanning for ESP32...")
    devices = await BleakScanner.discover()
    esp_address = None
    
    for d in devices:
        if d.name == ESP32_NAME:
            esp_address = d.address
            print(f"Found ESP32 at {esp_address}")
            break
            
    if esp_address:
        async with BleakClient(esp_address) as client:
            print("Connected!")
            # Read data from the ESP32
            data = await client.read_gatt_char(CHARACTERISTIC_UUID)
            print(f"Initial Sensor Data: {data}")
    else:
        print("ESP32 not found.")

asyncio.run(scan_and_connect())
