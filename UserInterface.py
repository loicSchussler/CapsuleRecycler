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
isFirstPhase = True

def afficherImageSuivante(fen):
    global index,le,labelPicture,entryValid

    if (isEntryValid()):
        if (index < le-1):
            index += 1
        else:
            finishFirstPhase(fen)
            return;
    
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


def reset(w):
    for child in w.winfo_children():
        reset(child)
        child.destroy()
        
def resetAllWidget(x):
    reset(x)



def finishFirstPhase(fen):
    global saveInfos,labelPicture
    
    pickle.dump( saveInfos, open( "save.p", "wb" ) )
    getCapsuleColor.main()
    labelPicture.config(image=None)
    resetAllWidget(fen)
    initNewWidgets(fen)



#---------------------------------------Phase 2------------------------------------------------------
def initNewWidgets(fen):
    dimensionsOfThePicture = []

    
    canvas2 = Canvas(fen,width=1000,height = 2000)
    canvas2.pack()

    labelInstructions2 = Label(canvas2,text="Please choose the picture you want to build with caps.")
    labelInstructions2.pack()

    fen.update_idletasks()
    pictureFileName = filedialog.askopenfilename()

    labelInstructions2["text"] = "Please input the dimensions of the support you want to build the picture on in cm."

    labelErrorEntryHeight = Label(canvas2,text="",font=("Courrier",11))
    labelErrorEntryHeight.pack()

    labelEntryHeight = Label(canvas2,text="Height",font=("Courrier",20))
    labelEntryHeight.pack()
    
    entryHeight = Entry(canvas2,width=40)
    entryHeight.pack()

    labelErrorEntryWidth = Label(canvas2,text="",font=("Courrier",11))
    labelErrorEntryWidth.pack()

    labelEntryWidth = Label(canvas2,text="Width",font=("Courrier",20))
    labelEntryWidth.pack()

    entryWidth = Entry(canvas2,width=40)
    entryWidth.pack()
    
    submitButton2 = Button(canvas2,text="Submit",command=lambda:finishPhase2(entryHeight,entryWidth,labelErrorEntryHeight,labelErrorEntryWidth,dimensionsOfThePicture,pictureFileName))
    submitButton2.pack()




def isEntryHeightValid(entryHeight,labelErrorEntryHeight,dimensionsOfThePicture):
    verify = entryHeight.get()
    try:
        testNumber = int(verify)
        dimensionsOfThePicture.append(verify)
        return True
    except ValueError:
        labelErrorEntryHeight['text'] = "Please input a number."
        return False

def isEntryWidthValid(entryWidth,labelErrorEntryWidth,dimensionsOfThePicture):
    verify = entryWidth.get()
    try:
        testNumber = int(verify)
        dimensionsOfThePicture.append(verify)
        return True
    except ValueError:
        labelErrorEntryWidth['text'] = "Please input a number."
        return False

def saveDimensionsAndFileName(dimensionsOfThePicture,pictureFileName):
    f = open("Build_strategyCS/Build_strategyCS/capsInfos.txt",'a')
    f.write(pictureFileName+"\n"+dimensionsOfThePicture[0]+" "+dimensionsOfThePicture[1]+"\n")
    f.close()

def finishPhase2(entryHeight,entryWidth,labelErrorEntryHeight,labelErrorEntryWidth,dimensionsOfThePicture,pictureFileName):
    
     if (isEntryHeightValid(entryHeight,labelErrorEntryHeight,dimensionsOfThePicture) and isEntryWidthValid(entryWidth,labelErrorEntryWidth,dimensionsOfThePicture)):
         saveDimensionsAndFileName(dimensionsOfThePicture,pictureFileName)
         


#----------------------------------------------------------------------------------------------
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

buttonValidate = Button(canvas,text="Valider",command=lambda:afficherImageSuivante(fen))
buttonValidate.pack()

image = PIL.Image.open(pictures[index])
photo = PIL.ImageTk.PhotoImage(image)
labelPicture = Label(canvas,image=photo)
labelPicture.image = photo
labelPicture.pack()

fen.mainloop()







#-----------------------------------------------------------------------------


    
