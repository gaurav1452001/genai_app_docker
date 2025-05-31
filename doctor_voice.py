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
from elevenlabs import generate, save, set_api_key

ELEVEN_LABS_API_KEY = os.getenv("ELEVEN_LABS_API_KEY")
set_api_key(ELEVEN_LABS_API_KEY)

def text_to_speech_elevenlabs(input_text, output_filepath):
        audio = generate(
            text=input_text,
            voice="Sarah",
            model="eleven_turbo_v2",
            output_format="mp3_44100_128"
        )
        save(audio, output_filepath)
        print(f"Audio saved successfully to {output_filepath}")
        

input_text = "Hello, my name is Sarah and i am an awesome girl!"
text_to_speech_elevenlabs(input_text, output_filepath="response_elevenlabs.mp3")

#use model for text output to voice