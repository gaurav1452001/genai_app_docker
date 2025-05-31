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
input_text = "Hello, my name is Sarah and i am an awesome girl!"
text_to_speech_gtts(input_text, "response.mp3")


#setup1.b text to speech tts-model for response elevenlabs
import elevenlabs
from elevenlabs.client import ElevenLabs

ELEVEN_LABS_API_KEY = os.getenv("ELEVEN_LABS_API_KEY")

def text_to_speech_elevenlabs(input_text,output_path):
    client = ElevenLabs(api_key=ELEVEN_LABS_API_KEY)
    audio=client.text_to_speech.convert(
        text=input_text,
        voice_id="EXAVITQu4vr4xnSDxMaL",
        output_format="mp3_44100_128",
        model_id="eleven_multilingual_v2",
    )
    elevenlabs.save(audio, output_path)
text_to_speech_elevenlabs("This is a new girl next door",output_path="response_elevenlabs.mp3")

#use model for text output to voice