@app.route('/api/mp3tonotes', methods=['POST'])
def _api_mp3tonotes():
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

            return jsonify({'transcription': get_transcription()})
        else:
            return render_template('mp3tonotes.html')
    except Exception as e:
        return jsonify({'error': str(e)})

