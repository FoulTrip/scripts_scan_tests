import asyncio

from Bluetooth.handlers import chooseDevice, scanDevices
from Bluetooth.handlers.isDeviceAudio import isAudioDevice
from Bluetooth.handlers.isDeviceAvailable import isAvailable


async def main():
    """
    Main entry point for the application, providing a menu to scan and interact with Bluetooth devices.

    Functionality:
        1. Displays a menu with two options:
            - Option 1: Scan for audio devices only.
            - Option 2: Scan for all Bluetooth devices.
        2. Handles user input to select an option.
        3. For Option 1:
            - Attempts to scan for devices up to a maximum of 3 times.
            - Filters out audio devices from the scanned results.
            - If audio devices are found, prompts the user to choose a device and check its availability.
            - If no audio devices are found or scanning fails, retries the scan or informs the user of failure.
        4. For Option 2:
            - Attempts to scan for devices up to a maximum of 3 times.
            - Prompts the user to choose a device from the full list of scanned devices.
            - If scanning fails, retries or informs the user of failure.
        5. Resets the number of attempts if a valid option is chosen or if an invalid option is provided.
        6. Prints messages to guide the user through the process and handle errors.

    Notes:
        - The function uses a retry mechanism to handle potential failures during the scanning process.
        - It ensures that the number of attempts is reset upon successful completion or upon selection of a valid option.
    """
    attempts = 0
    max_attempts = 3

    while True:
        option = input(
            "Choose an option: \n1. Scan Audio Devices Only\n2. Scan All Devices\n"
        )
        if option == "1":
            while attempts < max_attempts:
                devices = await scanDevices()
                if devices:
                    audio_devices = [
                        device.address
                        for device in devices
                        if await isAudioDevice(device)
                    ]  # Identify audio devices
                    if audio_devices:
                        await chooseDevice(devices, audio_devices, isAvailable)
                        attempts = 0  # Reset attempts on success
                        break
                    else:
                        print("No audio devices found.")
                        break
                else:
                    attempts += 1
                    if attempts < max_attempts:
                        print("Failed to scan devices. Retrying...")
                    else:
                        print("Failed to scan devices after several attempts.")
                        break

        elif option == "2":
            while attempts < max_attempts:
                devices = await scanDevices()
                if devices:
                    await chooseDevice(devices, [], isAvailable)
                    attempts = 0  # Reset attempts on success
                    break
                else:
                    attempts += 1
                    if attempts < max_attempts:
                        print("Failed to scan devices. Retrying...")
                    else:
                        print("Failed to scan devices after several attempts.")
                        break

        else:
            print("Invalid option. Please choose 1 or 2.")
            attempts = 0  # Reset attempts if an invalid option is chosen


if __name__ == "__main__":
    asyncio.run(main())
