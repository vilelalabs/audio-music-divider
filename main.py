# ** converter de .mp3 para .wav

# DUAS OPÇÕES:	
    # OK Localizar timestamps nas quais o audio tem uma amplitude próxima de zero E:

    # 2 OK "seleciono" o aúdio do início até ponto do timestamp,
    #   OK salvo esse trecho em arquivo separado
    #   OK removo o audio salvo do arquivo original
    #   OK repetir até que o arquivo original esteja vazio

# salvar cada parte em um arquivo separado (** .wav caso tenha sido necessario converter)

# ** converter de volta para MP3 
# ** deletar arquivos .wav

# -----------------------------------------------------------------------------------------
from pydub import AudioSegment
import glob
import os
import divider as dv

filename = 'audio'

song = AudioSegment.from_mp3(f"{filename}.mp3")
song.export(f"{filename}.wav", format="wav")

dv.divideIntoParts(f"{filename}.wav")

files = glob.glob(f"output/*.wav")
for file in files:
    song = AudioSegment.from_wav(file)
    song.export(f"{file}.mp3", format="mp3")
    os.remove(file)

os.remove(f"{filename}.wav")