from pydub import AudioSegment
from pydub.effects import normalize
from random import randint

def getShow(vocals, music):
    vocals = AudioSegment.from_file(vocals, "mp3")
    vocals += 10
    vocals = vocals.low_pass_filter(4000)
    vocals = vocals.high_pass_filter(500)
    vocals = normalize(vocals)
    vocals += 3

    music = AudioSegment.from_file(music, "mp3")
    musicLen = len(music)
    showLen = 15 * 60 * 1000
    start = randint(0, musicLen - showLen - 1)
    music = music[start:start+showLen]

    music = normalize(music)

    vocalLen = len(vocals) + 5000

    # make the music quiet when the vocals start and back to normal when the vocals end
    quiet = -16
    music = music.fade(to_gain=quiet, start=0, duration=5000)
    music = music.fade(to_gain=16, start=vocalLen, duration=5000)
    music = music.fade_out(5000)

    # Combine the vocals and music
    vocals = AudioSegment.silent(duration=5000) + vocals + AudioSegment.silent(duration=10 * 60 * 1000)
    show = vocals.overlay(music)

    show.export("./templates/show.mp3", format="mp3")

    return "./templates/show.mp3"

if __name__ == "__main__":
    getShow("./templates/vocals.mp3", "./templates/music.mp3")