from flask import Flask, Response, render_template
from datetime import datetime
from src.show import getShow
import threading
import time

app = Flask(__name__)

filepath = "./templates/show.mp3"
staticpath = "./templates/static.mp3"
format = "mpeg"

buffersize = 1024

def updateShow():
    while True:
        now = datetime.now()
        hour = now.replace(hour=now.hour, minute=0, second=0, microsecond=0)
        seconds_since_hour = (now - hour).total_seconds()
        seconds_into_show = seconds_since_hour % (15 * 60)

        if seconds_into_show >= (13 * 60):
            threading.Thread(target=getShow, args=(filepath,)).start()
            time.sleep(10 * 60)
        else:
            time.sleep(30)

def deliverShow(offset):
    with open(f'{filepath}', 'rb') as feed:
        feed.seek(offset)
        data = feed.read(buffersize)
        while data:
            yield data
            data = feed.read(buffersize)
        print("Finished sending")

def deliverStatic():
    with open(f'{staticpath}', 'rb') as feed:
        data = feed.read(buffersize)
        while data:
            yield data
            data = feed.read(buffersize)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/feed")
def stream():
    length = 15 * 60

    now = datetime.now()
    hour = now.replace(hour=now.hour, minute=0, second=0, microsecond=0)
    seconds_since_hour = (now - hour).total_seconds()
    seconds_into_show = seconds_since_hour % length
    byterate = 16000
    offset = int(seconds_into_show * byterate)

    response = Response(deliverShow(offset), mimetype=f"audio/{format}")

    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    response.headers.pop("Content-Length", None)
    return response

@app.route("/show")
def show():
    response = Response(deliverShow(0), mimetype=f"audio/{format}")
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    response.headers.pop("Content-Length", None)
    return response

if __name__ == "__main__":
    # threading.Thread(target=updateShow).start()
    app.run()