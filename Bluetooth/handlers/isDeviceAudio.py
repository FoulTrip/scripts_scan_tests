from bleak import BleakClient
from bleak.backends.device import BLEDevice
import asyncio


async def isAudioDevice(device: BLEDevice) -> bool:
    """
    Asynchronously checks if a given Bluetooth device is an audio device based on its services.

    Args:
        device (BLEDevice): The Bluetooth device to check.

    Returns:
        bool: True if the device is identified as an audio device, False otherwise.

    Functionality:
        1. Attempts to connect to the Bluetooth device using `BleakClient` with a timeout of 20 seconds.
        2. Retrieves the list of services offered by the device.
        3. Iterates over the services and prints each service's UUID.
        4. Checks if any of the service UUIDs match known audio service UUIDs, including:
            - A2DP (Advanced Audio Distribution Profile)
            - HFP / HSP (Hands-Free Profile / Headset Profile)
            - AVRCP (Audio/Video Remote Control Profile)
            - PBAP (Phone Book Access Profile)
            - Audio Sink, Source, and Endpoint
        5. Returns `True` if any of the service UUIDs match the known audio UUIDs, indicating the device is an audio device.
        6. Handles `asyncio.TimeoutError` if the connection times out, printing a timeout message.
        7. Catches and prints any other exceptions that occur during the process.

    Notes:
        - The function uses `async with` to ensure proper resource management of the `BleakClient`.
    """
    try:
        async with BleakClient(device, timeout=20.0) as client:
            services = await client.get_services()
            for service in services:
                print(f"Service found: {service.uuid}")
                if service.uuid in [
                    "0000110a-0000-1000-8000-00805f9b34fb",  # A2DP
                    "00001108-0000-1000-8000-00805f9b34fb",  # HFP / HSP
                    "0000110e-0000-1000-8000-00805f9b34fb",  # AVRCP
                    "0000112f-0000-1000-8000-00805f9b34fb",  # PBAP
                    "00001812-0000-1000-8000-00805f9b34fb",  # Audio Sink
                    "00001813-0000-1000-8000-00805f9b34fb",  # Audio Source
                    "00001816-0000-1000-8000-00805f9b34fb",  # Audio Endpoint
                ]:
                    return True
    except asyncio.TimeoutError:
        print(f"Timeout while connecting to {device.name}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return False
