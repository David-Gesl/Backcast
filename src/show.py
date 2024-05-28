from script import getScript
from tts import getVocal
from ytmusic import getMusic
from retrofy import retrofy

# from random import randint # for backup music

def getShow(output):
    talk = getScript()

    vocals = getVocal(talk)

    music = getMusic()

# music = f"./templates/music{randint(1, 3)}.mp3" # for backup music
    show = retrofy(vocals, music, output)
    return show

if __name__ == "__main__":
    getShow("./templates/show_test.mp3")