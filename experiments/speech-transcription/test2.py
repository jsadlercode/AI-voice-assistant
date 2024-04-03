import sys
import pyaudio
import wave
from faster_whisper import WhisperModel
import os
import time

def transcribe_chunk(model, file_path):
    segments, info = model.transcribe(file_path, beam_size=5)
    transcription = ' '.join(segment.text for segment in segments)
    return transcription

def record_chunk(p, stream, file_path, chunk_length=1):
    frames = []
    for _ in range(0, int(16000 / 1024 * chunk_length)):
        data = stream.read(1024)
        frames.append(data)

    wf = wave.open(file_path, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(16000)
    wf.writeframes(b''.join(frames))
    wf.close()

def transcribe_file(model, file_path):
    print(f"Transcribing file: {file_path}")
    transcription = transcribe_chunk(model, file_path)
    print(transcription)
    return transcription

def main2():
    # Check if a filename is provided as a command-line argument
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = None

    # Choose your model settings, change compute type to int8 if Mac or Float16 if you have a dedicated GPU.
    # Add attribute 'device="cuda"' if you have a dedicated Nvidia GPU
    model_size = "base.en"
    model = WhisperModel(model_size, compute_type="int8")

    if file_path:
        # Transcribe the provided audio file
        transcription = transcribe_file(model, file_path)
        with open("log.txt", "w") as log_file:
            log_file.write(transcription)
    else:
        # Live transcription from the microphone
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=4096)
        accumulated_transcription = ""  # Initialize an empty string to accumulate transcriptions

        try:
            while True:
                chunk_file = "temp_chunk.wav"
                record_chunk(p, stream, chunk_file)
                transcription = transcribe_chunk(model, chunk_file)
                print(transcription)
                os.remove(chunk_file)
                
                # Append the new transcription to the accumulated transcription
                accumulated_transcription += transcription + " "

        except KeyboardInterrupt:
            print("Stopping...")
            # Write the accumulated transcription to the log file
            with open("log.txt", "w") as log_file:
                log_file.write(accumulated_transcription)
        finally:
            print("LOG:" + accumulated_transcription)
            stream.stop_stream()
            stream.close()
            p.terminate()

if __name__ == "__main__":
    main2()
