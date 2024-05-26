import yt_dlp
from yt_dlp.utils._utils import MaxDownloadsReached
import random
import datetime

URLS = ["https://youtube.com/playlist?list=PLkRNa08en8VwGZAmeDszJeajSpM23bCVD&si=8aTDsf8JIJKM2P_d"] # retro music playlist

random.seed(int(datetime.datetime.now().timestamp()))

ydl_opts = {
    'paths': {'home':'./retromusic'},
    'playlistrandom':'True',
    'max_downloads':'1',
    'format': 'mp3/bestaudio/best',
    'postprocessors': [{  # Extract audio using ffmpeg
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
    }]
}

def downloadMusic():
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download(URLS)
        except MaxDownloadsReached as e:
            return
