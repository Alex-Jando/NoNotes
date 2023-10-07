import os
from pydub import AudioSegment
import speech_recognition as sr
from pydub.silence import split_on_silence 

# segmentation by silence method
# this method has better results, but only works if there isn't any background noise/music
def transcription_generator_by_silence():
    # cleanup previous transcription
    if os.path.exists('res/transcription.txt'):
        os.remove('res/transcription.txt')

    audio = AudioSegment.from_file('res/audio.wav')

    print(f'Length {len(audio)} | Loudness: {audio.dBFS}')

    output_directory = 'res/audio_chunks'

    chunks = split_on_silence(audio, min_silence_len=500, silence_thresh=-40, keep_silence=1000)

    r = sr.Recognizer()

    with open('res/transcription.txt', 'a') as output_file:
        for i, chunk in enumerate(chunks):
            chunk.export(f'{output_directory}/chunk_{i}.wav', format='wav')

            with sr.AudioFile(f'{output_directory}/chunk_{i}.wav') as source:
                try:
                    audio_data = r.record(source)
                    output_file.write(r.recognize_google(audio_data) + '\n')
                    print(f"Progress: {i + 1}/{len(chunks)}")
                except sr.UnknownValueError:
                    print(f"Progress: {i + 1}/{len(chunks)} - audio not recognized")
                except sr.RequestError as e:
                    print(f"Progress: {i + 1}/{len(chunks)} - request err: {e}")

            os.remove(f'{output_directory}/chunk_{i}.wav')


# segmentation by time method
# this works but it sometimes cuts off words, and is kind of worse ngl
def transcription_generator(audio_path='res/audio.wav'):
    # cleanup previous transcription
    if os.path.exists('res/transcription.txt'):
        os.remove('res/transcription.txt')

    max_segment_length = 15  # seconds

    r = sr.Recognizer()

    with sr.AudioFile(audio_path) as source:
        audio_duration = source.DURATION
        
        # segments needed
        num_segments = int(audio_duration / max_segment_length) + 1
    
    with sr.AudioFile(audio_path) as segment_source:
        for i in range(num_segments):
            start_time = i * max_segment_length
            end_time = min((i + 1) * max_segment_length, audio_duration)

            # audio segment
            segment_audio = r.record(segment_source, duration=end_time - start_time, offset=start_time)

            segment_transcript = ''
            try:
                # progress
                print(f"Progress: {i + 1}/{num_segments}")
                # recognize each segment
                segment_transcript = r.recognize_google(segment_audio)
            except sr.UnknownValueError:
                print(f"Segment {i + 1} could not be transcribed.")
            except sr.RequestError as e:
                print(f"Request error for segment {i + 1}: {e}")

            # Open and close the file for each write operation
            with open('res/transcript.txt', 'a') as f:
                f.write(segment_transcript + '\n')

# for converting audio formats (ffmpeg required)
def audio_converter(filename='audio', type='mp3'):
    folder='res/'

    audio = AudioSegment.from_mp3(f'{folder}{filename}.mp3')

    # Make sure old audio.flac is deleted
    if os.path.exists(f'{folder}audio.flac'):
        os.remove(f'{folder}audio.flac')

    audio.export(f'{folder}audio.flac', format="flac")

    # wait till file exists
    while not os.path.exists("f'{folder}audio.flac"):
        pass

