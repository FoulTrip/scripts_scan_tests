import asyncio


def displayDevices(devices, audio_devices, check_availability):
    """
    Displays a list of Bluetooth devices along with their status.

    Args:
        devices (list): A list of Bluetooth devices to display.
        audio_devices (set): A set of addresses of Bluetooth devices that are recognized as audio devices.
        check_availability (function): An asynchronous function that checks if a device is available.

    Functionality:
        1. Prints a header "Devices found:".
        2. Iterates over the list of devices.
        3. For each device, checks if its address is in the `audio_devices` set to determine if it is an audio device.
        4. Uses `asyncio.run` to execute the asynchronous `check_availability` function in a synchronous context to determine if the device is available.
        5. Prints the device details, including its address, name, whether it is an audio device, and its availability status.

    Notes:
        - `asyncio.run` is used here to run the asynchronous `check_availability` function from a synchronous context. This is generally not recommended in production code due to potential issues with event loop management, but it is used here for simplicity.
    """
    print("Devices found: ")
    for i, device in enumerate(devices):
        is_audio = "true" if device.address in audio_devices else "false"
        # Use asyncio.run in a synchronous context
        is_available = (
            "true"
            if asyncio.run(check_availability(device))
            else "false" if check_availability else ""
        )
        print(
            f"{i + 1}: Address: {device.address}, Name: {device.name}, IsDeviceAudio: {is_audio}, Available: {is_available}"
        )
