# Audio Music Divider

**⚠ ATTENTION: Actually CLI version using (main.py) works far better! GUI need improvements! ⚠**

See notes about downloading video in the OBSERVATIONS section.

### Description

Allows you to divide MP3 audio files into multiple parts based on silent found between them.

## Version 2.0 (GUI) - Beta

⚠ The 2.0 version has a GUI interface, so its not needed to add filename or params to command line. (in Windows) Just double-click in GUI at dist folder:
```bash
    ./dist/GUI.exe
```

## How to use v 1.0 (see before 08/19/2022)

- Use the following command to divide audio files:

```
    python3 main.py <filename.mp3> --mms <minimum_music_samples> --thr <threshold> --std <silent_time_detection>
```
## Customized Params

| Parameter             | Argument |    Default       | Time Equivalence (approx)  |Explanation |
|:---------------------:|:--------:|:----------------:|:-----------------:|:------------|
| Minimum Music Samples | ``--mms``    |    1.000,000 |  20.8 seconds     | Minimum samples to be counted as a music  |
| Threshold             | ``--thr``    |     0.001    |     -             | Minimum sample amplitude to be considered as silent |
| Silent Time Detection | ``--std``    |     49.000   |   1 second        | Minimum sample counts of silent to do a cut  |

All parameters are directly proportional (bigger number =  bigger attribute[time or amplitude])

## Tips on using

- If it's not getting to cut and output is just one or two .mp3 files, consider to increase **Threshold** value manually (good try, for example, it can be 0.005 to start), if it's cutting in a lot of pieces, decrease this value.
- Maybe the gap between songs are short, for this cases, decrease **Silent Time Detection** value.
- **Minimum Music Samples** can help to ignore tiny songs or some transitions between them.

---

### OBSERVATIONS: 
- The default values are good for most cases.
    - if audio has at least _1 second_ of silent parts between bigger audio parts (_more than 20s_), file will be correctly cutted on this parts.
    </br></br>
- All arguments are **optional**, if not specified, the default values will be used for those (not specified)arguments.
</br></br>

- ``--help`` will show the help message with short description for possible arguments. **(only CLI version)**

- Downloading videos: Actually our solution is not working, for that, now,  we recommend to download from one of this websites: [Save From Net](https://en1.savefrom.net/102-youtube-music-downloader-10up.html) or [YT5S](https://yt5s.biz/en200/youtube-to-mp3). close any pop ups and newew pages that will open and keep clicking on 'download button' until the file download start. This websites can go down at any time. We are not owners of this websites so we have any responsability for anything that can happen by visiting, downloading or any actions in the websites and not responsible for any of their functionality.

---

### FUTURE FEATURES

**BASIC**
- Create better UX for GUI version (GUI version seems broken for some reason - so now it's a fix to be done)
- Add Warning about trying to execute conversion in a lot big files (actually works good in .mp3 files below 150Mb).
- Work with multiple files
- Add way to choose output folder
- Create project integration with [ydc](https://github.com/vilelalabs/ydc) [possible cancelled - this project isn't working anymore]

**ADVANCED**
- Detect automatically the best params by checking whole audio file for silent/lowest amplitude parts before cutting (this can remove all needing for params).