from script import getScript
from tts import getVocal
from ytmusic import getMusic
from retrofy import getShow
from random import randint

talk = getScript()

vocals = getVocal(talk)

# will fix this later
# music = getMusic()

# get a random music files from the templates folder
music = f"./templates/music{randint(1, 3)}.mp3"

show = getShow(vocals, music)

