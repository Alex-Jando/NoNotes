import os
from pydub import AudioSegment
import speech_recognition as sr


r = sr.Recognizer()

def convert_mp3_to_wav(audio_path):
    print("Converting MP3 to WAV...")
    converted_audio_path = audio_path.replace('.mp3', '.wav')
    audio = AudioSegment.from_mp3(audio_path)
    audio.export(converted_audio_path, format="wav")
    os.remove(audio_path) # remove original mp3
    print("Conversion complete.")
    return converted_audio_path

def transcription_generator(filename):
    max_segment_length = 10
    transcript = ""
    audio_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'uploads', filename)
    print(audio_path)

    if audio_path.endswith('.mp3'):
        audio_path = convert_mp3_to_wav(audio_path)

    with sr.AudioFile(audio_path) as source:
        audio_duration = source.DURATION
        num_segments = int(audio_duration / max_segment_length) + 1  # segments needed

    for i in range(num_segments):
        start_time = i * max_segment_length
        end_time = min((i + 1) * max_segment_length, audio_duration)

        # audio segment
        with sr.AudioFile(audio_path) as segment_source:
            segment_audio = r.record(segment_source, duration=end_time - start_time, offset=start_time)

            transcript_segment = try_recognize(segment_audio, num_segments, i)
            transcript += transcript_segment + '\n' 

    os.remove(audio_path)
    return transcript

def try_recognize(audio, max, i):
    t = ''
    print(f"Progress: {i + 1}/{max}")
    try:
        t = r.recognize_google(audio)
    except sr.UnknownValueError:
        print(f"No transcription for {i + 1}.")
    except sr.RequestError as e:
        print(f"Request error for segment {i + 1}: {e}")
    return t
