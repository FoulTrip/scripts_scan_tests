import asyncio
from bleak.backends.device import BLEDevice
from bleak import BleakClient


async def isAvailable(device: BLEDevice) -> bool:
    """
    Asynchronously checks if a given Bluetooth device is currently connected.

    Args:
        device (BLEDevice): The Bluetooth device to check.

    Returns:
        bool: True if the device is connected, False otherwise.

    Functionality:
        1. Attempts to connect to the Bluetooth device using `BleakClient` with a timeout of 20 seconds.
        2. Checks if the connection to the device is established by accessing the `is_connected` property of the `BleakClient`.
        3. Returns `True` if the device is connected, `False` otherwise.
        4. Handles `asyncio.TimeoutError` if the connection times out, printing a timeout message.
        5. Catches and prints any other exceptions that occur during the process.

    Notes:
        - The function uses `async with` to ensure proper resource management of the `BleakClient`.
    """
    try:
        async with BleakClient(device, timeout=20.0) as client:
            return client.is_connected
    except asyncio.TimeoutError:
        print(f"Timeout while connecting to {device.name}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return False
