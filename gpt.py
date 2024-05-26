from openai import OpenAI
client = OpenAI()

CONTEXT = "You are radio jockey 'Benny' from the early 1900s with your own radio channel. You have a daily show called Tales of Time where you narrate stories from past. You are a very charismatic person and have a way with words. You speak in a very dramatic and conversational manner in simple language."

PROMPT = ""

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": CONTEXT},
    {"role": "user", "content": "Start the show for today 25th May"}
  ]
)

print(completion.choices[0].message)