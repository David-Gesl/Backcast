from flask import Flask, Response
from datetime import datetime
import os

app = Flask(__name__)

# filename = "final_audio_4kHz.wav"
# filename = "final_audio.wav"

# filename = "final_audio_8kHz.mp3"
# filename = "final_audio.mp3"

# filename = "final_audio.ogg"

# filename = "final_audio.aac"

# filename = "final_audio.opus"

# filename = "final_audio_openai_8kHz.mp3"
filename = "final_audio_openai.mp3"

format = "mpeg"
# format = "wav"
# format = "ogg"
# format = "aac"
# format = "opus"
buffersize = 1024

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/feed")
def stream():
    # now = datetime.now()
    # seconds_since_midnight = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
    # offset = int((seconds_since_midnight % 55) * 15898)
    def generate():
        with open(f"./templates/{filename}", "rb") as feed:
            # feed.seek(offset)
            data = feed.read(buffersize)
            while data:
                yield data
                data = feed.read(buffersize)
    return Response(generate(), mimetype=f"audio/{format}")

if __name__ == "__main__":
    app.run(host="0.0.0.0",
            debug=True,
            port=3000)