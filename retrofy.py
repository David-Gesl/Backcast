from pydub import AudioSegment
from pydub.effects import normalize

# from OpenAITTS import get_voice
from GoogleTTS import get_voice
from gpt import get_script

from datetime import datetime

# Get the script for today's show
talks = get_script()

# merge the content for intro and first event and merge the outro with the last event
intro = talks[0]["content"]
outro = talks[-1]["content"]

filenames = []

for i, talk in enumerate(talks[1:len(talks)-1]):
    if i == 0:
        text = intro + talk["content"]
    elif i == len(talks)-3:
        text = talk["content"] + outro
    else:
        text = talk["content"]
    filenames.append(get_voice(f"output{i+1}.mp3", text))

back = AudioSegment.from_file("backtrack.mp3", "mp3")

# Load the audio files
audioList = [AudioSegment.from_file(f, "mp3") for f in filenames]

# Combine the audio files
combined = AudioSegment.empty()
combined += AudioSegment.silent(duration=5000)
for audio in audioList:
    combined += audio
    combined += AudioSegment.silent(duration=10 * 60 * 1000)
combined += AudioSegment.silent(duration=5000)

# Add some distortion by increasing the volume and then applying a high-pass filter
combined += 10

# make it retro
combined = combined.low_pass_filter(1000)
combined = combined.high_pass_filter(500)

# Normalize the audio
combined = normalize(combined)

# Combine the distorted audio with the backtrack
final_audio = combined.overlay(back)

# Apply fade in and fade out effects
final_audio = final_audio.fade_in(3000).fade_out(3000)

# get todays date
today = datetime.now().strftime("%d-%m")
# Export the modified audio
final_audio.export(f"./{today}/final_audio.mp3", format="mp3")