# Audio Music Divider

Allows you to divide MP3 audio files into multiple parts based on silent found between them.

## Version 2.0 (GUI)

⚠ The 2.0 version has a GUI interface, so its not needed to add filename or params to command line. Just run as:
```
    python3 main.py
```

## How to use v 1.0 (see before 08/19/2022)

- Use the following command to divide audio files:

```
    python3 main.py <filename.mp3> --mms <minimum_music_samples> --thr <threshold> --std <silent_time_detection>
```
## Customized Params

| Parameter             | Argument |    Default       | Time Equivalence (approx)  |Explanation |
|:---------------------:|:--------:|:----------------:|:-----------------:|:------------|
| Minimum Music Samples | ``--mms``    |    1.000.000 |  20.8 seconds     | Minimum samples to be counted as a music  |
| Threshold             | ``--thr``    |     0.001    |     -             | Minimum sample amplitude to be considered as silent |
| Silent Time Detection | ``--std``    |     49.000   |   1 second        | Minimum sample counts of silent to do a cut  |

### Observations: 
- The default values are good for most cases.
    - if audio has at least _1 second_ of silent parts between bigger audio parts (_more than 20s_), file will be correctly cutted on this parts.
    </br></br>
- All arguments are **optional**, if not specified, the default values will be used for those (not specified)arguments.
</br></br>

- ``--help`` will show the help message with short description for possible arguments. **(only not GUI version)**