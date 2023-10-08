import os
from pydub import AudioSegment
import speech_recognition as sr
from pydub.silence import split_on_silence 

script_dir = os.path.abspath(os.path.dirname(__file__))
project_dir = os.path.abspath(os.path.join(script_dir, '..'))
r = sr.Recognizer()

TRANSCRIPTION_OUTPUT_DIR = os.path.join(project_dir, 'res', 'transcription.txt')
SOURCE_AUDIO_DIR = os.path.join(project_dir, 'uploads', 'audio.wav')

def clear_transcription():
    # delete previous transcription
    if os.path.exists(TRANSCRIPTION_OUTPUT_DIR):
        os.remove(TRANSCRIPTION_OUTPUT_DIR)
    # create new transcription file
    with open(TRANSCRIPTION_OUTPUT_DIR, 'w+') as f:
        f.write('')

# better transcription accuracy but cannot handle music/background noise
def transcription_generator_by_silence():
    clear_transcription()

    audio = AudioSegment.from_file(SOURCE_AUDIO_DIR)

    print(f'Length {len(audio)} | Loudness: {audio.dBFS}')

    output_directory = 'res/audio_chunks'
    if not os.path.exists(output_directory):
        os.mkdir(output_directory)

    chunks = split_on_silence(audio, min_silence_len=500, silence_thresh=-40, keep_silence=1000)

    for i, chunk in enumerate(chunks):
        chunk.export(f'{output_directory}/chunk_{i}.wav', format='wav')

        with sr.AudioFile(f'{output_directory}/chunk_{i}.wav') as source:
            audio_data = r.record(source)
            transcription=''

            try_recognize(audio_data, len(chunks), i)
            
            with open(TRANSCRIPTION_OUTPUT_DIR, 'a+') as f:
                    f.write(transcription + '\n')     
        
        os.remove(f'{output_directory}/chunk_{i}.wav') # remove temp chunk
    
    os.rmdir(output_directory) # remove temp directory
        
# sometimes words get cut, but can handle noise
def transcription_generator(audio_path=SOURCE_AUDIO_DIR):
    clear_transcription()

    max_segment_length = 10  # Maximum segment length in seconds

    with sr.AudioFile(audio_path) as source:
        audio_duration = source.DURATION
        num_segments = int(audio_duration / max_segment_length) + 1 # segments needed

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

# for converting audio formats (ffmpeg required)
def audio_converter(filename='audio', type='mp3'):
    folder = 'uploads/'

    audio = AudioSegment.from_mp3(f'{folder}{filename}.mp3')

    # Make sure old audio.flac is deleted
    if os.path.exists(f'{folder}audio.flac'):
        os.remove(f'{folder}audio.flac')

    audio.export(f'{folder}audio.flac', format="flac")

    # wait till file exists
    while not os.path.exists("f'{folder}audio.flac"):
        pass

def get_transcription():
    if os.path.exists(TRANSCRIPTION_OUTPUT_DIR):
        with open(TRANSCRIPTION_OUTPUT_DIR, 'r') as f:
            return f.read()
    else:
        return None

# transcription_generator()