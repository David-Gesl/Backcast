from flask import Flask, Response, render_template
from datetime import datetime
from src.show import getShow
import threading

app = Flask(__name__)

filepath = "./templates/show.mp3"
staticpath = "./templates/static.mp3"
format = "mpeg"

buffersize = 1024

newShowRequested_lock = threading.Lock()
newShowRequested = False

def deliverShow(offset):
    with open(f"{filepath}", "rb") as feed:
        feed.seek(offset)
        data = feed.read(buffersize)
        while data:
            yield data
            data = feed.read(buffersize)

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
    show_length = 13 * 60
    length = 15 * 60

    now = datetime.now()
    hour = now.replace(hour=now.hour, minute=0, second=0, microsecond=0)
    seconds_since_hour = (now - hour).total_seconds()
    seconds_into_show = seconds_since_hour % length
    byterate = 16000

    offset = int(seconds_into_show * byterate)

    global newShowRequested
    if seconds_into_show < show_length:
        with newShowRequested_lock:
            newShowRequested = False
        return Response(deliverShow(offset), mimetype=f"audio/{format}")
    else:
        with newShowRequested_lock:
            if not newShowRequested:
                newShowRequested = True
                # start a new thread to generate a new show
                threading.Thread(target=getShow, args=(filepath,)).start()
        return Response(deliverStatic(), mimetype=f"audio/{format}")

@app.route("/noise")
def noise():
    return Response(deliverStatic(), mimetype=f"audio/{format}")

@app.route("/show")
def show():
    return Response(deliverShow(0), mimetype=f"audio/{format}")

if __name__ == "__main__":
    app.run()