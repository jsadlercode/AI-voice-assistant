import whisper
import numpy as np
import sounddevice as sd

def transcribe_audio():
    # Load the Whisper model
    model = whisper.load_model("base")

    # Set up the audio stream
    sample_rate = 16000
    duration = 5.0  # Duration of each audio chunk in seconds

    print("Listening...")

    while True:
        try:
            # Record audio from the microphone
            audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float32')
            sd.wait()

            # Transcribe the audio using Whisper
            result = model.transcribe(audio.flatten())

            # Print the transcribed text
            print("Transcription: " + result["text"])

        except KeyboardInterrupt:
            break

# Start the live transcription
transcribe_audio()