
from pydub import AudioSegment
import glob
import os
import divider as dv

import sys

# # standard parameters
# mms = 1000000
# thr = 0.001
# std = 49000

# # get parameters from command line
# filename = (sys.argv[1]  if len(sys.argv) > 1 else None)

# for i in range(2, len(sys.argv)):
#     if sys.argv[i] == "--mms":
#         mms = int(sys.argv[i+1])
#     if sys.argv[i] == "--thr":
#         thr = float(sys.argv[i+1])
#     if sys.argv[i] == "--std":
#         std = int(sys.argv[i+1])
#     if sys.argv[i] == "--help":
#         print("Possible arguments:")
#         print("--mms: minimum music samples")
#         print("--thr: threshold")
#         print("--std: silent time detection")
#         print("--help: show this help")
#         print(" Go to project on github (https://github.com/vilelalabs/audio-music-divider) for more details.")
#         exit()

# if(not filename):
#     print("No file specified, use: python3 main.py <filename.mp3> ...args \nExiting...")
#     exit()

def prepareFile(filename):

    print("Loading file...")
    song = AudioSegment.from_mp3(filename)

    print("Cleaning up output folder...")
    files = glob.glob(f"output/*")
    for file in files:
        os.remove(file)

    print("Converting file to wav...")
    wavFilename = filename.replace(".mp3", ".wav")

    song.export(wavFilename, format="wav")
    return wavFilename

def finishProcess(wavFilename):
    print("Converting to mp3 and erasing wav files...",end='')
    files = glob.glob(f"output/*.wav")
    for file in files:
        print(".",end='', flush=True)
        song = AudioSegment.from_wav(file)
        song.export(f"{file[0:-4]}.mp3", format="mp3")
        os.remove(file)
    os.remove(wavFilename)
    print("\nDone!")

# EXECUTION
# prepareFile(filename)
# dv.divideIntoParts(wavFilename, mms, thr, std)
# finishProcess(wavFilename)
