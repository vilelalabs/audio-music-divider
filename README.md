# Audio Music Divider

Allows you to divide audio files into multiple parts based on silent found between them.


## How to use

- Put on same folder of main.py a MP3 file named "audio" (the extension must be .mp3)
ex: "audio.mp3"
- if audio has at least 1 second of silent parts between bigger audio parts (more than 20s), file will be correctly cutted on this parts.

### Customize the cut:

- in divider.py its possible to adjust **threshold** for silence detection, **time in silent** and **minimum audio length** to be cutted.

### Next Updates
- [X] Bash Info
- [ ] Filename in args
- [ ] Erase previous converted files (clear output folder)
- [ ] Remove ".wav" text in .mp3 output files
- [ ] Basic GUI
