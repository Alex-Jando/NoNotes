from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
from pydub import AudioSegment
import os

script_dir = os.path.abspath(os.path.dirname(__file__))
project_dir = os.path.abspath(os.path.join(script_dir, '..'))

TRANSCRIPTION_OUTPUT_DIR = os.path.join(project_dir, 'res', 'transcription.txt')
SOURCE_AUDIO_DIR = os.path.join(project_dir, 'res', 'small_audio.wav')

def transcription_generator(audio_path=SOURCE_AUDIO_DIR):
    if os.path.exists(TRANSCRIPTION_OUTPUT_DIR):
        os.remove(TRANSCRIPTION_OUTPUT_DIR)
    with open(TRANSCRIPTION_OUTPUT_DIR, 'w+') as f:
        f.write('')

    max_segment_length = 30

    client = speech.SpeechClient()

    with open(audio_path, 'rb') as audio_file:
        content = audio_file.read()

    audio_duration = get_audio_duration(content)
    num_segments = int(audio_duration / max_segment_length) + 1  # segments needed

    for i in range(num_segments):
        start_time = i * max_segment_length
        end_time = min((i + 1) * max_segment_length, audio_duration)

        audio_segment = content[start_time:end_time]

        transcript = try_recognize_google(client, audio_segment, num_segments, i)

        with open(TRANSCRIPTION_OUTPUT_DIR, 'a') as f:
            f.write(transcript + '\n')
            f.flush()

def try_recognize_google(client, audio_segment, total_segments, current_segment):
    audio = types.RecognitionAudio(content=audio_segment)
    config = types.RecognitionConfig(
        language_code="en-US",
        enable_automatic_punctuation=True,
    )

    try:
        response = client.recognize(config=config, audio=audio)
        transcript = ""
        for result in response.results:
            transcript += result.alternatives[0].transcript
        print(f"Progress on segment {current_segment + 1}/{total_segments}")
        return transcript
    except Exception as e:
        print(f"Error in segment {current_segment + 1}/{total_segments}: {str(e)}")
        return ""

def get_audio_duration(audio_content):
    audio = AudioSegment.from_buffer(audio_content)
    return len(audio) / 1000.0