
import numpy as np
import soundfile as sf


def divideIntoParts(fileName, mms= 1000000, thr= 0.001, std = 49000):

    data, samplerate = sf.read(fileName)

    selectedData = np.zeros((len(data), 2))
    
    countLowData = 0
    cut_point = len(data)-1
    
    minimum_music_samples = mms # default 1000000 -  aprox 20.8s of music
    threshold = thr             # default 0.001  
    silent_time_detection = std # default 49000 - approx 1s of silence        
    i = 0

    # while there is data to be processed
    print("Working on file...",end='')
    while len(data) > minimum_music_samples: 
        for x in range(len(data)):

            if x >= minimum_music_samples: 
                if(data[x][0] < threshold and data[x][1] < threshold and data[x][0] > -threshold and data[x][1] > -threshold):
                    countLowData += 1
                    if(countLowData >= silent_time_detection):
                        cut_point = x

            selectedData[x][0] = data[x][0]
            selectedData[x][1] = data[x][1]
        
            # ponto de corte do áudio
            if x >= cut_point:
                print(".",end='', flush=True)
                break

        # save final audio output
        dataToSave = selectedData[0:cut_point]
        sf.write(f'output/music{i}.wav', dataToSave, samplerate)

        # remove processed data from original file
        newAudioToAnalyze = data[cut_point:len(data)]
        data = newAudioToAnalyze

        # restart global variables
        countLowData = 0
        cut_point = len(data)-1
        i += 1