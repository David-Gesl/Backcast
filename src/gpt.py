from openai import OpenAI
from datetime import datetime
from dotenv import load_dotenv
import json

load_dotenv()

client = OpenAI()

CONTEXT = "You are radio jockey 'Benny' from the early 1900s with your own radio channel. You have a daily show called Tales of Time where you narrate stories from past. You are a very charismatic person and have a way with words. You speak in a very dramatic and conversational manner in simple language. The show's format covers three main topics - 1. Historical Events (Important inventions or scientific discoveries made on that day), 2. Cultural Milestones (Iconic moments in film, music, or literature, like the release of a famous movie or book. Major sports achievements or memorable games that took place on that day.), 3. Anecdotes and Stories (Narrating stories about quirky historical things received from the audeience of the show)."

JSON_FORMAT = """
{
  "responses": [
    {
      "topic": "Introduction",
      "content": "introduction_content short"
    },
    {
      "topic": "HistoricalEvents",
      "content": "historical_events_content atleast 500 words"
    },
    {
      "topic": "CulturalMilestones",
      "content": "cultural_milestones_content at least 500 words"
    },
    {
      "topic": "AnecdotesAndStories",
      "content": "anecdotes_and_stories_content at least 500 words"
    },
    {
      "topic": "Outro",
      "content": "outro_content short"
    }
  ]
}
"""

PROMPT = f"Today is ${datetime.now().strftime("%d %m")}. Generate narrator's script (don't use any newlines, emojis) for today's show in JSON format containing an array of responses (introduction, historical events, cultural milestones, anecdotes and stories, outro). Every response should be a string of 500 words except introduction and outro. JSON format should be like this:" + JSON_FORMAT


def get_script() -> list:
  completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
      {"role": "system", "content": CONTEXT},
      {"role": "user", "content": PROMPT}
    ]
  )

  response_str = completion.choices[0].message.content
  obj = json.loads(response_str)
  # print(obj)
  return obj.get("responses")