import os
from pydub import AudioSegment
import speech_recognition as sr

script_dir = os.path.abspath(os.path.dirname(__file__))
project_dir = os.path.abspath(os.path.join(script_dir, '..'))
r = sr.Recognizer()

TRANSCRIPTION_OUTPUT_DIR = os.path.join(project_dir, 'res', 'transcription.txt')
SOURCE_AUDIO_DIR = os.path.join(project_dir, 'res', 'audio.mp3')


def clear_transcription():
    # delete previous transcription
    if os.path.exists(TRANSCRIPTION_OUTPUT_DIR):
        os.remove(TRANSCRIPTION_OUTPUT_DIR)
    # create a new transcription file
    with open(TRANSCRIPTION_OUTPUT_DIR, 'w+') as f:
        f.write('')

def transcription_generator(audio_path=SOURCE_AUDIO_DIR):
    clear_transcription()

    max_segment_length = 10

    if audio_path.endswith('.mp3'):
        print("Converting MP3 to WAV...")
        converted_audio_path = audio_path.replace('.mp3', '.wav')
        audio = AudioSegment.from_mp3(audio_path)
        audio.export(converted_audio_path, format="wav")
        audio_path = converted_audio_path

        while not os.path.exists(audio_path.replace('.mp3', '.wav')):
            pass

    with sr.AudioFile(audio_path) as source:
        audio_duration = source.DURATION
        num_segments = int(audio_duration / max_segment_length) + 1  # segments needed

    for i in range(num_segments):
        start_time = i * max_segment_length
        end_time = min((i + 1) * max_segment_length, audio_duration)

        # audio segment
        with sr.AudioFile(audio_path) as segment_source:
            segment_audio = r.record(segment_source, duration=end_time - start_time, offset=start_time)

            transcript = try_recognize(segment_audio, num_segments, i)

            with open(TRANSCRIPTION_OUTPUT_DIR, 'a') as f:
                f.write(transcript + '\n')
                f.flush()

    # if was converted from MP3 to WAV, remove the temporary WAV file
    if audio_path != SOURCE_AUDIO_DIR:
        os.remove(audio_path)

def try_recognize(audio, max, i):
    t=''
    print(f"Progress: {i + 1}/{max}")
    try:
        t = r.recognize_google(audio)
    except sr.UnknownValueError:
        print(f"No transcription for {i + 1}.")
    except sr.RequestError as e:
        print(f"Request error for segment {i + 1}: {e}")
    return t

def get_transcription():
    if os.path.exists(TRANSCRIPTION_OUTPUT_DIR):
        with open(TRANSCRIPTION_OUTPUT_DIR, 'r') as f:
            return f.read()
    else:
        return None

transcription_generator()