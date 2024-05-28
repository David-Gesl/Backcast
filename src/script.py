from openai import OpenAI
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

CONTEXT = "You are a radio host in the early 1900s. You have a show called 'On this day' which talks about fun stories from the past that happened on this day. Fun stories include inventions, discoveries, historical events, films, music, anecdotes from audience, etc. You talk in a very friendly and engaging way."

PROMPT = f"Today is {datetime.now().strftime('%d %B')}. Write what you are going to say in 500 words. Don't introduce yourself, just start talking about the fun stories from the past that happened on this day."

def getScript():
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": CONTEXT},
      {"role": "user", "content": PROMPT}
    ]
  )
  response_str = completion.choices[0].message.content
  return response_str