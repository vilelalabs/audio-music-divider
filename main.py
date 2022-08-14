
from pydub import AudioSegment
import glob
import os
import divider as dv

filename = 'audio'

print("Loading file...")
song = AudioSegment.from_mp3(f"{filename}.mp3")
print("Converting file to wav...")
song.export(f"{filename}.wav", format="wav")

dv.divideIntoParts(f"{filename}.wav")
print("\n")

print("Converting to mp3 and erasing wav files...",end='')
files = glob.glob(f"output/*.wav")
for file in files:
    print(".",end='', flush=True)
    song = AudioSegment.from_wav(file)
    song.export(f"{file}.mp3", format="mp3")
    os.remove(file)
os.remove(f"{filename}.wav")
print("\nDone!")