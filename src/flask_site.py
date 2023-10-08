from flask import Flask, render_template, request, redirect, jsonify
from transcription_generator import transcription_generator as tg
from transcription_generator import TRANSCRIPTION_OUTPUT_DIR, get_transcription
import os

app = Flask(__name__, template_folder='templates')

<<<<<<< Updated upstream
@app.route('/mp3tonotes', methods=['POST', 'GET'])
def mp3tonotes():
    return render_template('mp3tonotes.html')
    
    
@app.route('/api/mp3tonotes', methods=['POST'])
def _api_mp3tonotes():
    try:
        file = request.files['audio']
        if file:
            file.save('../uploads/audio.wav')
            
            # create transcription
            tg()
=======
@app.route('/')
def home():
    return(render_template('home.html'))

@app.route('/notes')
def home():
    return(render_template('notes.html'))

@app.route('/confirm-save')
def home():
    return(render_template('home.html'))

@app.route('/')
def home():
    return(render_template('home.html'))
>>>>>>> Stashed changes

            # wait until transcription is done
            while get_transcription() is None:
                pass
            
            os.remove('../uploads/audio.wav')

            return jsonify({'transcription': get_transcription()})
        else:
            return render_template('mp3tonotes.html')
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/notes')
def _notes():
    return(render_template('home.html'))
@app.route('/confirmsave')
def _confirmsave():
    return(render_template('home.html'))
@app.route('/')
def _():
    return redirect('/mp3tonotes')
    # return(render_template('home.html'))

app.run(debug=True, host='localhost', port=80)