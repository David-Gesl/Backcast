from openai import OpenAI
from dotenv import load_dotenv
from datetime import datetime
import os
load_dotenv()
client = OpenAI()

def get_voice(filename, text):
  # make a new folder for today's date
  today = datetime.now().strftime("%d-%m")
  if not os.path.exists(f"./templates/{today}"):
    os.mkdir(f"./templates/{today}")
  fname = filename
  pname = f"./templates/{today}/"

  response = client.audio.speech.create(
    model="tts-1-hd",
    voice="onyx",
    input=text
  )

  response.write_to_file(pname + fname)

  return pname+fname

if __name__ == "__main__":
  get_voice("introduction", "Hello, I am Benny, your radio jockey from the early 1900s. Welcome to Tales of Time, your daily dose of history, culture, and stories. Today is 15th August, and we have a lot of interesting things to talk about. Let's get started.")