from flask import Flask, Response
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/mp3")
def streammp3():
    now = datetime.now()
    seconds_since_midnight = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
    offset = int((seconds_since_midnight % 55) * 15898)
    def generate():
        with open("./templates/final_audio.mp3", "rb") as fmp3:
            fmp3.seek(offset)
            data = fmp3.read(512)
            while data:
                yield data
                data = fmp3.read(512)
    return Response(generate(), mimetype="audio/mpeg")

@app.route("/mp3nostream")
def mp3():
    def file():
        with open("./templates/final_audio.mp3", "rb") as fmp3:
            return fmp3.read()
    return Response(file(), mimetype="audio/mpeg")

if __name__ == "__main__":
    app.run(host="0.0.0.0",
            debug=True,
            port=3000)