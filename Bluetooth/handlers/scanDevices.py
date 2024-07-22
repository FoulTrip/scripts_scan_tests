from bleak import BleakScanner


async def scanDevices():
    """
    Asynchronously scans for nearby Bluetooth devices.

    Returns:
        list: A list of discovered Bluetooth devices.

    Functionality:
        1. Prints a message indicating that the scan for Bluetooth devices is starting.
        2. Uses the `BleakScanner.discover()` method to scan for nearby Bluetooth devices.
        3. Returns the list of discovered devices.
        4. Catches and prints any exceptions that occur during the scanning process.
        5. Returns an empty list if an error occurs during the scan.

    Notes:
        - This function uses asynchronous programming to perform the device scan without blocking other operations.
    """
    print("Scanning for nearby Bluetooth devices...")
    try:
        devices = await BleakScanner.discover()
        return devices
    except Exception as e:
        print(f"An error occurred while scanning devices: {e}")
        return []
