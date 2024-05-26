from pydub import AudioSegment
from pydub.effects import normalize

# Load your audio file
audio = AudioSegment.from_file("output1.mp3", "mp3")
back = AudioSegment.from_file("backtrack.mp3", "mp3")

# Normalize the audio (optional, but can help)
normalized_audio = normalize(audio)

# Add some distortion by increasing the volume and then applying a high-pass filter
distorted_audio = normalized_audio + 10
distorted_audio = distorted_audio.high_pass_filter(2000)

# added a 5 second silence to the distorted audio
distorted_audio = AudioSegment.silent(duration=5000) + distorted_audio + AudioSegment.silent(duration=5000)

# Combine the distorted audio with the backtrack
final_audio = distorted_audio.overlay(back)

# Apply fade in and fade out effects
final_audio = final_audio.fade_in(2000).fade_out(2000)

# Export the modified audio
final_audio.export("final_audio.mp3", format="mp3")