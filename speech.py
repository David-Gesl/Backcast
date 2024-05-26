"""Synthesizes speech from the input string of text or ssml.
Make sure to be working in a virtual environment.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""
from google.cloud import texttospeech

# Instantiates a client
client = texttospeech.TextToSpeechClient()

# Set the text input to be synthesized
input_text = "Ladies and gentlemen, gather 'round your radios! On this fine day, May 25th, let’s travel back to the year 1895. Picture a world buzzing with innovation and wonder. On this very day, the dynamic duo of the Lumière brothers, Auguste and Louis, dazzled Parisian audiences with the first public screening of their revolutionary invention: the Cinématographe. Imagine the gasps of astonishment as moving pictures danced on the screen, bringing scenes of bustling city life to vivid reality. It was the dawn of a new era in entertainment, and the world of cinema was born! Now, doesn’t that just make your heart race with excitement?"

synthesis_input = texttospeech.SynthesisInput(text=input_text)

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US", 
    name="en-US-Journey-D",
    ssml_gender=texttospeech.SsmlVoiceGender.MALE
)

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

# The response's audio_content is binary.
with open("output.mp3", "wb") as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')