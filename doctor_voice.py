#setup1.a text to speech tts-model for response gTTS
import os
from gtts import gTTS

def text_to_speech_gtts(input_text, output_path):
    language = 'en'

    audioobj=gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_path)
input_text = "Hello, how can I assist you today?"
text_to_speech_gtts(input_text, "response.mp3")


#setup1.b text to speech tts-model for response elevenlabs
import elevenlabs
from elevenlabs.client import ElevenLabs

def text_to_speech_gtts(input_text, output_path):
    language = 'en'

    audioobj=gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_path)
input_text = "Hello, how can I assist you today?"
text_to_speech_gtts(input_text, "response.mp3")

#use model for text output to voice