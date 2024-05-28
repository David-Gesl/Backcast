from script import getScript
from tts import getVocal
from ytmusic import getMusic
from retrofy import getShow
from random import randint

print("Getting script...")
talk = getScript()

print("Getting vocals...")
vocals = getVocal(talk)

# will fix this later
print("Getting music...")
# music = getMusic()

# get a random music files from the templates folder
music = f"./templates/music{randint(1, 3)}.mp3"

print("Generating show...")
show = getShow(vocals, music)
print("Finished generating show.")

