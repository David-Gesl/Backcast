from google.cloud import texttospeech

client = texttospeech.TextToSpeechClient()

def getVocal(text):

    synthesis_input = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", 
        name="en-US-Journey-D",
        ssml_gender=texttospeech.SsmlVoiceGender.MALE
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    pathname = "./templates/"
    filename = "vocals.mp3"

    with open(pathname+filename, "wb") as out:
        out.write(response.audio_content)

    return pathname+filename