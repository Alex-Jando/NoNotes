from flask import Flask, render_template, request, redirect, jsonify
from transcription import transcription_generator as tg
from summarize import summarize_text
from database import add_note, get_note, get_notes, update_note, delete_note, delete_all_notes
import os
import requests

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['POST', 'GET'])
def _():
    return render_template('index.html')
    
    
@app.route('/api/mp3tonotes', methods=['POST'])
def _api_mp3tonotes():

    try:

        file = request.files['audio']

        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'uploads', file.filename))

        transcription = tg(file.filename)

        response = requests.post('http://bark.phon.ioc.ee/punctuator', data = {'text': transcription})

        if not response.ok:

            raise Exception('Error adding punctuation to transcription!')
        
        notes = summarize_text(response.text)

        return jsonify({'transcription': response.text, 'notes': ''.join([f'<li>{bullet}</li>' for bullet in notes])})
    
    except Exception as e:

        return jsonify({'error': str(e)})

@app.route('/api/addnote', methods=['POST'])
def _api_addnote():

    print(request.json)

    form = request.json

    title = form['title'] or 'New Note'
    text = form['text']
    notes = form['notes']

    try:

        token = add_note(title, text, notes)

        return jsonify({'success': True, 'token': token})

    except:

        return jsonify({'success': False, 'error': 'Unable to save note!'})

@app.route('/notes', methods=['GET'])
def _get_notes():

    return render_template('notes.html', notes=get_notes())

@app.route('/temp_page')
def _temp_page():
    return render_template('home.html')


@app.route('/home')
def _home():
    return render_template('home.html')


@app.route('/confirmsave')
def _confirmsave():
    return render_template('notes.html')

app.run(debug=True, host='localhost', port=80)