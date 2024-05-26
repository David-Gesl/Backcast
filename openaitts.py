from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
client = OpenAI()

speech_file_path = "output1.mp3"

input_text = "Ladies and gentlemen, gather 'round your radios! On this fine day, May 25th, let’s travel back to the year 1895. Picture a world buzzing with innovation and wonder. On this very day, the dynamic duo of the Lumière brothers, Auguste and Louis, dazzled Parisian audiences with the first public screening of their revolutionary invention: the Cinématographe. Imagine the gasps of astonishment as moving pictures danced on the screen, bringing scenes of bustling city life to vivid reality. It was the dawn of a new era in entertainment, and the world of cinema was born! Now, doesn’t that just make your heart race with excitement?"

response = client.audio.speech.create(
  model="tts-1-hd",
  voice="onyx",
  input=input_text
)

response.write_to_file(speech_file_path)