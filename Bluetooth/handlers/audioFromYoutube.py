import os
from pytube import YouTube
from pydub import AudioSegment
from pydub.playback import play


async def playAudioFromYouTube(url: str):
    """
    Plays the audio from a YouTube video given its URL.

    Args:
        url (str): The URL of the YouTube video from which to extract the audio.

    Functionality:
        1. Receives a YouTube URL as an argument.
        2. Uses the `pytube` library to create a `YouTube` object for the given URL.
        3. Filters the video streams to get the audio stream.
        4. Downloads the audio stream as an MP4 file to a temporary location.
        5. Converts the MP4 file to an audio format that `pydub` can handle.
        6. Plays the audio using `pydub.playback.play`.
        7. Removes the temporary file after playback to avoid leaving unnecessary files.

    Exceptions:
        If an error occurs during downloading or playback, it catches the exception and prints an error message.
    """
    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        file_path = audio_stream.download(filename="audio.mp4")
        audio = AudioSegment.from_file(file_path, format="mp4")
        os.remove(file_path)  # Remove the file after converting

        play(audio)  # Play the audio

    except Exception as e:
        print(f"An error occurred while downloading or playing the audio: {e}")
