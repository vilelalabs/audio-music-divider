# Audio Music Divider

Allows you to divide MP3 audio files into multiple parts based on silent found between them.


## How to use

- Use the following command to divide audio files:

```
    python3 main.py <filename.mp3> --mms <minimum_music_samples> --thr <threshold> --std <silent_time_detection>
```
Where:

| Argument |    Default      |  Explanation |
|:--------:|:---------------:|:------------|
| ``--mms``    |    1.000.000  | Minimum samples to be counted as a music  |
| ``--thr``    |     0.001     |   Minimum sample amplitude to be considered as silent |
| ``--std``    |     49.000    |    Minimum sample counts of silent to do a cut  |

### Observations: 
- The default values are good for most cases.
- For samples consider the **approximated** values:
    - 1.000.000 samples = 20,8 seconds
    - 49.000 samples = 1 second

- if audio has at least _1 second_ of silent parts between bigger audio parts (_more than 20s_), file will be correctly cutted on this parts.

- All arguments are **optional**, if not specified, the default values will be used for those (not specified)arguments.

- ``--help`` will show the help message with short description for possible arguments.