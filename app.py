from flask import Flask, render_template, jsonify,request
from ai_logic import encode_image, image_to_text, record_audio, transcribe_audio, text_to_speech_gtts
import os
from werkzeug.utils import secure_filename
import uuid

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
UPLOAD_FOLDER = 'image_uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/audio_to_text', methods=['GET'])
def find_answer():
    try:
        audio_path = "patient_audio.mp3"
        record_audio(file_path=audio_path)
        GROQ_KEY = os.getenv("GROQ_API_KEY")
        stt_model = "whisper-large-v3"
        transcribed_text = transcribe_audio(stt_model, audio_path, GROQ_KEY)
        print(f"Transcribed text: {transcribed_text}")
        return jsonify({
            'success': True,
            'transcribed_text': transcribed_text
        })
        
    except Exception as e:
        print(f"Error in find_answer: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500
    
@app.route('/image_to_text', methods=['GET','POST'])
def analyse_image():
    try:
        query="Analyze the image and provide insights."
        model="meta-llama/llama-4-scout-17b-16e-instruct"
        if request.method == 'POST':
            file = request.files['image']  # this holds the uploaded image in memory
            if file:
                filename = secure_filename(file.filename)
                image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(image_path)
                print(f"Image saved to {image_path}")
        encoded_image=encode_image(image_path)
        image_text=image_to_text(query,model,encoded_image)
        return jsonify({
            'success': True,
            'image_text': image_text
        })
        
    except Exception as e:
        print(f"Error in analyse_image: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=8000)