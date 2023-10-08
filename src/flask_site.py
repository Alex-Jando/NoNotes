from flask import Flask, render_template, request, redirect
from transcription_generator import transcription_generator as tg
from transcription_generator import TRANSCRIPTION_OUTPUT_DIR, get_transcription
import os

app = Flask(__name__, template_folder='templates')

@app.route('/mp3tonotes', methods=['POST', 'GET'])
def mp3tonotes():
    if request.method == 'POST':
        try:
            file = request.files['audio']
            if file:
                file.save('../uploads/audio.wav')
                
                # create transcription
                tg()

                # wait until transcription is done
                while get_transcription() is None:
                    pass
                
                os.remove('../uploads/audio.wav')
                return render_template('mp3tonotes.html', message='success', transcription=get_transcription())
            else:
                return render_template('mp3tonotes.html')
        except Exception as e:
            return "An error occurred: " + str(e)
    else:
        return render_template('mp3tonotes.html')
        
app.run(debug=True, host='localhost', port=80)