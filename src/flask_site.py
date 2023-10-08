from flask import Flask, render_template, request, redirect, jsonify
from transcription_generator import transcription_generator as tg
from transcription_generator import TRANSCRIPTION_OUTPUT_DIR, get_transcription
import os

app = Flask(__name__, template_folder='templates')

@app.route('/mp3tonotes', methods=['POST', 'GET'])
def mp3tonotes():
    return render_template('mp3tonotes.html')
    
    
@app.route('/api/mp3tonotes', methods=['POST'])
def _api_mp3tonotes():
    
    try:

        file = request.files['audio']

        file.save('../uploads/audio.wav')
            
        tg()

        while get_transcription() is None:
            pass
        
        os.remove('../uploads/audio.wav')

        return jsonify({'transcription': get_transcription()})
    
    except Exception as e:

        return jsonify({'error': str(e)})

@app.route('/')
def _home():
    return(render_template('home.html'))

@app.route('/notes')
def _notes():
    return(render_template('home.html'))

@app.route('/confirm-save')
def _confirm_save():
    return(render_template('notes.html'))

app.run(debug=True, host='localhost', port=80)