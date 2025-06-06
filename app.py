from flask import Flask, render_template, jsonify
from ai_logic import encode_image, image_to_text, record_audio, transcribe_audio, text_to_speech_gtts
import os

app = Flask(__name__)

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/find_answer', methods=['GET'])
def find_answer():
    try:
        # Record audio from microphone
        audio_path = "patient_audio.mp3"
        record_audio(file_path=audio_path)
        
        # Transcribe the recorded audio
        GROQ_KEY = os.getenv("GROQ_API_KEY")
        stt_model = "whisper-large-v3"
        transcribed_text = transcribe_audio(stt_model, audio_path, GROQ_KEY)
        
        # Store transcribed text (you can use session or database later)
        # For now, we'll just process it
        print(f"Transcribed text: {transcribed_text}")
        
        # Redirect back to home page
        return render_template('base.html', transcribed_text=transcribed_text)
        
    except Exception as e:
        print(f"Error in find_answer: {str(e)}")
        return render_template('base.html', error=str(e))


if __name__ == '__main__':
    app.run(debug=True, port=8000)