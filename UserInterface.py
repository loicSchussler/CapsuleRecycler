import sys
import tkinter
import PIL
import glob
import os
import pickle
import subprocess
import getCapsuleColor

from PIL import Image, ImageTk ## Importation des modules utiles dans PIL
from tkinter import filedialog
from tkinter import *



index = 0
isNbInput = False

def afficherImageSuivante():
    global index,le,labelPicture,entryValid,fen

    if (isEntryValid()):
        if (index < le-1):
            index += 1
        else:
            finishFirstPhase()
    
        labelPicture.destroy()
        image = PIL.Image.open(pictures[index])
        photo = PIL.ImageTk.PhotoImage(image)
        labelPicture = Label(image=photo)
        labelPicture.image = photo
        
        labelPicture.pack()
        entryValid = False
        labelErrorMessage['text'] = ""


        

def saveNumberInput(number):
    global index,saveInfos

    saveInfos[str(index)] = {"numberOfCaps": number}
    

    
        

def isEntryValid():
    global numberOfThisKindOfCaps,labelErrorMessage, entryValid

    verify = numberOfThisKindOfCaps.get()
    try:
        testNumber = int(verify)
        saveNumberInput(verify)
        return True
    except ValueError:
        labelErrorMessage['text'] = "Veuillez entrer un nombre."
        return False

def finishFirstPhase():
    global saveInfos
    
    pickle.dump( saveInfos, open( "save.p", "wb" ) )
    getCapsuleColor.main()


fen = Tk()
fen.attributes('-fullscreen',True)

#---------------------------------------------------------------------------
canvas = Canvas(fen,width=1000,height = 2000)
canvas.pack()
#-----------------------------------------------------------------------------
labelInputCapsPicture = Label(canvas, text = "Please choose a folder of caps picture",font=("Courrier",11))
labelInputCapsPicture.pack()

labelErrorMessage = Label(canvas, text="")
labelErrorMessage.pack()

numberOfThisKindOfCaps = Entry(canvas,width=40)
numberOfThisKindOfCaps.pack()

fen.update_idletasks()

folder_input = filedialog.askdirectory()
saveInfos = { "folderPath": folder_input}

pictures = glob.glob(os.path.join(folder_input, '*.jpg'))

le = len(pictures)

buttonValidate = Button(canvas,text="Valider",command=afficherImageSuivante)
buttonValidate.pack()

image = PIL.Image.open(pictures[index])
photo = PIL.ImageTk.PhotoImage(image)
labelPicture = Label(image=photo)
labelPicture.image = photo
labelPicture.pack()

fen.mainloop()







#-----------------------------------------------------------------------------


    
