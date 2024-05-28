from src.script import getScript
from src.tts import getVocal
from src.ytmusic import getMusic
from src.retrofy import retrofy

# from random import randint # for backup music

def getShow(output):
    print("Getting show")
    talk = getScript()

    vocals = getVocal(talk)

    music = getMusic()

    # music = f"./templates/music{randint(1, 3)}.mp3" # for backup music
    show = retrofy(vocals, music, output)
    print("Show ready")
    return show

if __name__ == "__main__":
    getShow("./templates/show_test.mp3")