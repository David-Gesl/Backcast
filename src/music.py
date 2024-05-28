import yt_dlp
from yt_dlp.utils._utils import MaxDownloadsReached
import random
import datetime

# URLS = ["https://youtube.com/playlist?list=PLkRNa08en8VwGZAmeDszJeajSpM23bCVD&si=8aTDsf8JIJKM2P_d"] # retro music playlist
URLS = ["https://youtube.com/playlist?list=PLz1WANnSJES9Yesv3Wk7kSjD7VTcGdLxw&si=my-QbfjxBmdLOoD8"]

random.seed(int(datetime.datetime.now().timestamp()))

def download_ranges(info_dict, ydl):
    # Example video sections to download
    sections = [
        {"start_time": 0, "end_time": 900},
    ]

    return sections

ydl_opts = {
    'paths': {'home':'./templates'},
    'playlistrandom':'True',
    'max_downloads':'1',
    'download_ranges': download_ranges,
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
        
if __name__ == "__main__":
    downloadMusic()
