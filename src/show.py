from script import getScript
from tts import getVocal
from ytmusic import getMusic
from retrofy import retrofy
import gc

# from random import randint # for backup music

def getShow(output):
    print("Getting show")
    talk = getScript()
    gc.collect()

    print("Getting vocals")
    vocals = getVocal(talk)
    gc.collect()

    print("Getting music")
    music = getMusic()
    gc.collect()

    print("Retrofying")
    # music = f"./templates/music{randint(1, 3)}.mp3" # for backup music
    show = retrofy(vocals, music, output)
    gc.collect()
    print("Show ready")
    return show

if __name__ == "__main__":
    getShow("./templates/show_test.mp3")