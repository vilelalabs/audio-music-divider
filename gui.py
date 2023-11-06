# links úteis:
# https://docs.python.org/3/library/dialog.html#module-tkinter.filedialog


from tkinter import *
from tkinter import filedialog as fd
#from tkinter.ttk import *

import divider
import amd

def selectFile():
    filename = fd.askopenfilename(initialdir = "/",
        title = "Select file",filetypes = (("mp3 files","*.mp3"),("all files","*.*")))

    entryFile.delete(0,END)
    #entryFile.insert(0,filename.split('/')[-1]) # without path
    entryFile.insert(0,filename) # with path

def getValuesToParams():
    global mms
    global thr
    global std
    mms = int(entryMms.get() if entryMms.get() else 1000000)
    thr = float(entryThr.get() if entryThr.get() else 0.001)
    std = int(entryStd.get() if entryStd.get() else 49000)

def divide():
    global filename
    global wavFilename
    filename = entryFile.get()
    getValuesToParams()

    wavFilename = amd.prepareFile(filename)
    outputQuantity = divider.divideIntoParts(wavFilename, mms, thr, std)
    amd.finishProcess(wavFilename)

    entryOutput.delete(0,END)
    entryOutput.insert(0,outputQuantity)


window = Tk()
window.title("Audio Music Divider")
window.geometry('640x480')
#window.resizable(False, False)
window.resizable(width=1, height=1)

#imports
backgroundImg = PhotoImage(file="img\\background.png")
browseBtnImg = PhotoImage(file="img\\browse.png")
divideBtnImg = PhotoImage(file="img\\divide.png")

#labels
backgroundLabel = Label(window, image=backgroundImg)
backgroundLabel.pack()


# File selection
entryFile = Entry(window, bd=2, font=("Calibri",15), justify=LEFT)
entryFile.place(width=211,height=38, x=148, y=98)

btnBrowser = Button(window, bd=0, image=browseBtnImg, command=selectFile)
btnBrowser.place(width=56,height=50, x=515, y=80)


# Additional Parameters
entryMms = Entry(window, font=("Calibri",13), justify=RIGHT)
entryMms.place(width=156,height=29, x=422, y=177)
entryThr = Entry(window, font=("Calibri",13), justify=RIGHT)
entryThr.place(width=156,height=29, x=422, y=237)
entryStd = Entry(window, font=("Calibri",13), justify=RIGHT)
entryStd.place(width=156,height=29, x=422, y=297)


#Divide Button
btnDivide = Button(window, bd=0, image=divideBtnImg, command=divide)
btnDivide.place(width=140,height=40, x=292, y=360)


#Output Info
entryOutput = Entry(window, font=("Calibri",12), justify=CENTER)
entryOutput.place(width=45,height=23, x=440, y=433)

window.mainloop()