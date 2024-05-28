from pytube import Playlist
import random
from pytube.innertube import _default_clients

_default_clients["ANDROID_MUSIC"] = _default_clients["ANDROID_CREATOR"]

# PLAYLIST_URL = "https://youtube.com/playlist?list=PLkRNa08en8VwGZAmeDszJeajSpM23bCVD&si=8aTDsf8JIJKM2P_d"

PLAYLIST_URL = "https://youtube.com/playlist?list=PLz1WANnSJES9Yesv3Wk7kSjD7VTcGdLxw&si=my-QbfjxBmdLOoD8"

def getMusic():
    playlist = Playlist(PLAYLIST_URL)
    video = random.choice(playlist.videos)
    audiostream = video.streams.filter(only_audio=True).first()
    audiostream.download(output_path="./templates/", filename="music.mp3")
    return "./templates/music.mp3"

if __name__ == "__main__":
    getMusic()