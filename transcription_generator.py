import os
from pydub import AudioSegment
import speech_recognition as sr

# # Convert wav file into flac
# audio = AudioSegment.from_mp3("audio.mp3")

# # Make sure old audio.flac is deleted
# if os.path.exists("audio.flac"):
#     os.remove("audio.flac")

# audio.export("audio.flac", format="flac")

# # Wait for the file conversion to finish
# while not os.path.exists("audio.flac"):
#     pass  # Wait until the file exists

# -----pt 1 works, pt 2 works, but pt 1 + 2 doesn't! yay! ------ #

audio = 'res/Mitosis.wav'
max_segment_length = 20  # Maximum segment length in seconds

r = sr.Recognizer()

with sr.AudioFile(audio) as source:
    audio_duration = source.DURATION
    
    # segments needed
    num_segments = int(audio_duration / max_segment_length) + 1

# clear transcript.txt
if os.path.exists("transcript.txt"):
    os.remove("transcript.txt")

for i in range(num_segments):
    start_time = i * max_segment_length
    end_time = min((i + 1) * max_segment_length, audio_duration)

    # audio segment
    with sr.AudioFile(audio) as segment_source:
        segment_audio = r.record(segment_source, duration=end_time - start_time, offset=start_time)

        segment_transcript = ''
        try:
            # recognize each segnment
            segment_transcript = r.recognize_google(segment_audio)
        except sr.UnknownValueError:
            print(f"Segment {i + 1} could not be transcribed.")
        except sr.RequestError as e:
            print(f"Request error for segment {i + 1}: {e}")

        with open('res/transcript.txt', 'a') as f:
            f.write(segment_transcript + '\n')
            


