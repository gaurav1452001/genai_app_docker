#setup1.a text to speech tts-model for response gTTS
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
        else:
            raise OSError("Unsupported OS")
    except Exception as e:
        print(f"Error opening audio file: {e}")

input_text = "This is another test case for the text to speech conversion using gTTS."
text_to_speech_gtts(input_text=input_text, output_path="response.mp3")


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
    sound = AudioSegment.from_mp3("response_elevenlabs.mp3")
    sound.export("response_elevenlabs.wav", format="wav")
    os_name = platform.system()
    try:
        if os_name == "Darwin":
            subprocess.run(["afplay", output_path])
        elif os_name == "Windows":  # macOS
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "response_elevenlabs.wav").PlaySync();'])
        elif os_name == "Linux":  # Linux and other OS
            subprocess.run(["aplay", output_path])
        else:
            raise OSError("Unsupported OS")
    except Exception as e:
        print(f"Error opening audio file: {e}")

# Example usage
# input_text = "This is a test case and is only for testing purposes."
# text_to_speech_elevenlabs(input_text, output_path="response_elevenlabs.mp3")





