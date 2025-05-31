#1 setup audio recorder (ffmpeg and pyaudio)
import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def record_audio(file_path, timeout=10, phrase_time_limit=None):
    """Record audio for a specified duration and save it to a file."""
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            logging.info("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source,duration=1)
            logging.info("You can start speaking...")

            audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            logging.info("Recording is complete")

            wav_data= audio_data.get_wav_data()
            mp3_audio = AudioSegment.from_wav(BytesIO(wav_data))
            mp3_audio.export(file_path, format="mp3", bitrate="128k")

            logging.info(f"Audio saved to {file_path}")

    except Exception as e:
        logging.error(f"An error occurred while recording audio: {e}")

audio_path="patient_audio.mp3"
record_audio(file_path=audio_path)

#2 setup speech to text-stt-model for transcription
import os
from groq import Groq

GROQ_KEY = os.getenv("GROQ_API_KEY")
client=Groq(api_key=GROQ_KEY)
stt_model="whisper-large-v3"
transcription=client.audio.transcriptions.create(
    file=open(audio_path, "rb"),
    model=stt_model,
    language="en",
)
print("Transcription:", transcription.text)