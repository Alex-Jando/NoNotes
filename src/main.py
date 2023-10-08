from flask import Flask, render_template, request, redirect, jsonify

from transcription_mp3 import transcription_generator as tg
from summarize import summarize_text

import os
import requests

app = Flask(__name__, template_folder='templates')

@app.route('/mp3tonotes', methods=['POST', 'GET'])
def mp3tonotes():
    return render_template('mp3tonotes.html')
    
    
@app.route('/api/mp3tonotes', methods=['POST'])
def _api_mp3tonotes():
    
    try:

        file = request.files['audio']
        file.save('../uploads/' + file.filename)
        print(f"Saved file {file.filename}")
        transcription = tg(file.filename)

        response = requests.post('http://bark.phon.ioc.ee/punctuator', data = {'text': transcription})
        if not response.ok:
            raise Exception('Error adding punctuation to transcription!')
        summary = summarize_text(response.text)

        return jsonify({'summary': ''.join([f'<li>{bullet}</li>' for bullet in summary])})
    
    except Exception as e:

        return jsonify({'error': str(e)})

@app.route('/')
def _home():
    return(render_template('home.html'))

@app.route('/notes')
def _notes():
    return(render_template('home.html'))

@app.route('/confirmsave')
def _confirmsave():
    return(render_template('notes.html'))

app.run(debug=True, host='localhost', port=80)