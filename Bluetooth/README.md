# Bluetooth Device Scanner and Audio Player

## Overview
This project is designed to scan for Bluetooth devices, identify audio devices, and allow interaction with them, including playing audio from YouTube. It uses the `bleak` library for Bluetooth operations and `pytube` for handling YouTube audio.

## Features
 - `Scan for Bluetooth Devices: ` Identifies and lists nearby Bluetooth devices.
 - `Filter Audio Devices: ` Distinguishes audio devices from other Bluetooth devices.
 - `Check Device Availability: ` Verifies if a Bluetooth device is available.
 - `Play Audio from YouTube: ` Allows playing audio from a YouTube link through an identified audio device.

## Prerequisites
Ensure you have the following installed:

 - Python 3.7+
 - `bleak` library
 - `pytube` library
 - `pydub` library
 - `ffmpeg` (for audio processing with `pydub`)

Install the required Python libraries using pip:
```bash
pip install bleak pytube pydub
```

## Usage
 1. Run the script with Python
```bash 
python your_script_name.py
```
 2. Follow the prompts to choose an option and interact with Bluetooth devices.

## Notes
 - Ensure that your system has Bluetooth capabilities and that necessary permissions are granted.
 - The `pydub` library requires `ffmpeg` for audio file handling. Make sure `ffmpeg` is installed and accessible from your PATH.