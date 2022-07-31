
import numpy as np
import soundfile as sf




def divideIntoParts(fileName):

    data, samplerate = sf.read(fileName)

    selectedData = np.zeros((len(data), 2))

    
    countLowData = 0
    cut_point = len(data)-1
    
    minimum_music_samples = 1000000
    threshold = 0.001 # default 0.001  
    silent_time_detection = 49000 # default 49000        
    i = 0

    # while there is data to be processed
    while len(data) > minimum_music_samples: 
        for x in range(len(data)):

            # garante cortes apenas após o início da música (após aprox: 20,8 segundos)
            if x >= minimum_music_samples: 
                if(data[x][0] < threshold and data[x][1] < threshold and data[x][0] > -threshold and data[x][1] > -threshold):
                    countLowData += 1
                    # approx 1 second of low volume
                    if(countLowData >= silent_time_detection):
                        cut_point = x

            selectedData[x][0] = data[x][0]
            selectedData[x][1] = data[x][1]
        
            # ponto de corte do áudio
            if x >= cut_point:
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