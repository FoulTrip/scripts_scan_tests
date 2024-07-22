from Bluetooth.handlers import displayDevicesAsync
from Bluetooth.handlers.audioFromYoutube import playAudioFromYouTube


async def chooseDevice(devices, audio_devices, check_availability):
    """
    Allows the user to choose a device from a list of Bluetooth devices and perform actions based on their selection.

    Args:
        devices (list): A list of Bluetooth devices.
        audio_devices (set): A set of Bluetooth devices that are recognized as audio devices.
        check_availability (function): An asynchronous function that checks if a device is available.

    Functionality:
        1. Continuously displays the list of devices and their statuses using `displayDevicesAsync`.
        2. Prompts the user to select a device by entering its number or 'q' to quit.
        3. If the user inputs 'q', the function exits.
        4. Converts the user's choice into an index to select a device from the list.
        5. Checks if the selected device is an audio device and whether it is available.
        6. If the device is an audio device and available:
            - Prompts the user to choose an action (turn off, turn on, or connect).
            - If 'Connect' is chosen, asks the user for a YouTube URL and plays the audio from that URL using `playAudioFromYouTube`.
            - Prompts the user to enter a volume percentage and prints a message about the volume setting.
        7. If the device is not an audio device or not available, informs the user.
        8. Handles invalid input by informing the user of the error.

    Exceptions:
        - Handles `ValueError` if the user input cannot be converted to an integer and prints an error message.
    """
    while True:
        await displayDevicesAsync(devices, audio_devices, check_availability)
        choice = input(
            "Select the number of the device you want to check (or 'q' to quit): "
        )
        if choice.lower() == "q":
            print("Exiting...")
            return

        try:
            index = int(choice) - 1
            if 0 <= index < len(devices):
                selectedDevice = devices[index]
                is_audio = selectedDevice.address in audio_devices
                is_available = (
                    await check_availability(selectedDevice)
                    if check_availability
                    else ""
                )
                print(
                    f"You selected: Address: {selectedDevice.address}, Name: {selectedDevice.name}, IsDeviceAudio: {is_audio}, Available: {is_available}"
                )

                if is_audio and is_available:
                    print(
                        f"The device {selectedDevice.name} seems to be an audio device and is available."
                    )
                    action = input(
                        "Choose an option: \n1. Turn Off\n2. Turn On\n3. Connect\n"
                    )
                    if action == "3":
                        url = input("Enter the YouTube link of the song: ")
                        await playAudioFromYouTube(url)
                        volume = input("Enter the volume percentage (0-100): ")
                        print(
                            f"Volume set to {volume}% (note: actual adjustment might not be supported)."
                        )
                else:
                    print(
                        f"The device {selectedDevice.name} either does not seem to be an audio device or is not available."
                    )
            else:
                print("Invalid selection.")
        except ValueError:
            print("Invalid input.")
