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
from elevenlabs.client import ElevenLabs
from elevenlabs import save

def text_to_speech_elevenlabs(input_text, output_path):
    elevenlabs = ElevenLabs(
        api_key=os.getenv("ELEVEN_LABS_API_KEY"),
    )
    audio = elevenlabs.text_to_speech.convert(
        text=input_text,
        voice_id="EXAVITQu4vr4xnSDxMaL",
        model_id="eleven_turbo_v2",
        output_format="mp3_44100_128",
    )
    save(audio, output_path)

# Example usage
input_text = "Hello! I am a follower of Gaurav Kumar."
text_to_speech_elevenlabs(input_text, "response_elevenlabs2.mp3")

#use model for text output to voice