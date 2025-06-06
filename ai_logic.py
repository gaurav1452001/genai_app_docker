#doctor_logic.py, encode_image, image_to_text
import os
import base64
from groq import Groq
GROQ_KEY= os.getenv("GROQ_API_KEY")

def encode_image(image_path):
    image_file=open(image_path,"rb")
    return base64.b64encode(image_file.read()).decode("utf-8")

query="You are a doctor. Please analyze the image and provide a diagnosis based on the symptoms shown in the image. Please provide a detailed explanation of the condition and any recommended treatments."
model="meta-llama/llama-4-scout-17b-16e-instruct"
def image_to_text(query,model,encoded_image):
    messages=[
        {
            "role":"user",
            "content": [
                #image model has two queries, one text and one image
                {
                    #text query
                    
                    "type": "text",
                    "text": query
                },
                {
                    #image query

                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}"
                    }
                }
            ]
        }
    ]
    client=Groq()
    chat_response=client.chat.completions.create(
        messages=messages,
        model=model,
    )
    return chat_response.choices[0].message.content

#doctor_voice.py text_to_speech_gtts
import os
from gtts import gTTS
from pydub import AudioSegment
import subprocess
import platform

def text_to_speech_gtts(input_text, output_path):
    language = 'en'

    audioobj=gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_path)
    sound = AudioSegment.from_mp3("response.mp3")
    sound.export("response.wav", format="wav")
    os_name = platform.system()
    try:
        if os_name == "Darwin":
            subprocess.run(["afplay", output_path])
        elif os_name == "Windows":  # macOS
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "response.wav").PlaySync();'])
            # subprocess.run(['start', 'response.mp3'], shell=True)

        elif os_name == "Linux":  # Linux and other OS
            subprocess.run(["aplay", output_path])
        else:        raise OSError("Unsupported OS")
    except Exception as e:
        print(f"Error opening audio file: {e}")


#patient_logic.py record_audio,transcribe_audio
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

# Transcription function
import os
from groq import Groq

GROQ_KEY = os.getenv("GROQ_API_KEY")
stt_model="whisper-large-v3"
def transcribe_audio(stt_model,audio_path,GROQ_KEY):
    client=Groq(api_key=GROQ_KEY)
    transcription=client.audio.transcriptions.create(
        file=open(audio_path, "rb"),
        model=stt_model,
        language="en",
    )
    return transcription.text