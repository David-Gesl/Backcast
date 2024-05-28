from pydub import AudioSegment
from pydub.effects import normalize
from random import randint
import gc

def retrofy(vocals, music, output):
    print("Getting vocals")
    vocals = AudioSegment.from_file(vocals, "mp3")
    vocals += 10
    vocals = vocals.low_pass_filter(4000)
    vocals = vocals.high_pass_filter(500)
    vocals = normalize(vocals)
    vocals += 3
    gc.collect()

    print("Selecting music")
    import os, psutil; print(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)
    # Randomly select a 15 minute segment of the music
    music = AudioSegment.from_file(music, duration=900)
    print("Loaded music segment")
    # musicLen = len(music)
    # showLen = 15 * 60 * 1000
    # start = randint(0, musicLen - showLen - 1)
    # music = music[start:start+showLen]
    gc.collect()
    
    print("Normalizing")
    music = normalize(music)
    gc.collect()

    print("Getting vocal length")
    vocalLen = len(vocals) + 5000

    # make the music quiet when the vocals start and back to normal when the vocals end
    change = 16
    print("Fading music")
    music = music.fade(to_gain=-change, start=4000, duration=2000)
    print("fade1")
    gc.collect()
    music = music.fade(to_gain=change, start=vocalLen, duration=5000)
    print("fade2")
    gc.collect()
    music = music.fade_in(2000).fade_out(5000)
    print("fade3")
    gc.collect()

    print("Combining")
    # Combine the vocals and music
    vocals = AudioSegment.silent(duration=6000) + vocals
    show = music.overlay(vocals)
    gc.collect()

    show.export(output, format="mp3")

    return output

if __name__ == "__main__":
    retrofy("./templates/vocals.mp3", "./templates/music", "./templates/show_test.mp3")