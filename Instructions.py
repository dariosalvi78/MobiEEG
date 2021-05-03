'''
Instructions is guiding the user through some tasks. 
It also stores the time of each tasks been started and ended
There is a TimeSettings file which allows an admin to justify the time of each tasks and pauses

'''

from tkinter import *
from tkinter import messagebox
import os
import pygame
import random
import time
from PIL import ImageTk, Image
import datetime
import csv
import MobiClient as mc
import SignalGui as coca 
import EEGReadData as erd
import threading

fileWriter =''

t=3
counter = 0
pygame.init()
pygame.mixer.init()
mute = True
taskCounter = 0
arrowCounter = 10

def exGui():
# kills the thread for the datareeding from EEG. Stores a message in the event file and destroys the ui
    response = messagebox.askyesno(message=exMessage)
    if response == 1:
        erd.setMainConnection()
        mc.sendEvent("TC", "The task has been canceled by the user")
        checkInst(20)
        root.destroy()

def ex():
#Destroys the ui when the tasks are done
    global root
    root.destroy()

def disMute():
#Destroys the mute button and tells teh EEGReadData that the instruction has begun
    global btnMute
    btnMute.destroy()
    erd.setSendTrue()
    mc.setTime()

def runThread():
#Threads the instruction
    global t5
    t5 = threading.Thread(target=countDown)
    t5.start()
    coca.closeGui()

def countDown():
# Begins the instruction
    global lblCount
    global t
    global counter
    lblCount = Label(root, width=28, height=5, bg='black', fg='white')
    lblCount.grid(column=0, row=0)
    if t>-1:
        t=t-1
        GuiFrame.config(font=("Arial", 20), text='-')
        if t>-1:
            lblCount.configure(text=t+1, font=("Arial", 150), width=2, height=0)
            pygame.mixer.music.load("Sounds\SoftBeep.mp3")
            pygame.mixer.music.play()
            lblCount.after(1000, countDown)
        else:
            lblCount.configure(text='+', font=("Arial", 280), width=2, height=0)
            pygame.mixer.music.load("Sounds\SoftBeep2.mp3")
            pygame.mixer.music.play()
            lblCount.after(carmenCtrl, countDown)
    elif t==-1:
        counter = counter + 1
        checkInst(counter)

def instWriter(fWriterE):
# Receives a fileWriter and sets it as global so each instruction can be written on the file
    global fileWriterEvent
    fileWriterEvent = fWriterE

def checkInst(cc):
# Receives an int which decides which cunstruction should run
    global arrowCounter, taskCounter, mc, sgnlWriterE
    temp = datetime.datetime.now()
    time = str(temp.hour) +':'+ str(temp.minute)+':' + str(temp.second)+':'+str(temp.microsecond)
    sgnlWriterE = csv.writer(fileWriterEvent, delimiter=',', quotechar='"', 
    quoting=csv.QUOTE_MINIMAL)

    if cc==1:
        mc.sendEvent("KYEO", "Keep your eyes open started")
        sgnlWriterE.writerow([time, 'Keep your eyes open', ' Begins'])
        instrOpenEye()

    if cc==2:
        mc.sendEvent("KYEO", "Keep your eyes open ended")
        mc.sendEvent("KYEC", "Keep your eyes closed started")
        sgnlWriterE.writerow([time, 'Keep your eyes open', ' Ends'])
        sgnlWriterE.writerow([time, 'Keep your eyes closed', ' Begins'])
        instrCloseEye()

    if cc==3:
        mc.sendEvent("KYEc", "Keep your eyes closed ended")
        mc.sendEvent("P", "Pause started")
        sgnlWriterE.writerow([time, 'Keep your eyes closed', ' Ends'])
        sgnlWriterE.writerow([time, 'Pause', ' Begins'])
        instrPause(carmenB4Imagin) # It should be 3000 = 3 seconds

    if cc==4:
        mc.sendEvent("P", "Pause ended")
        mc.sendEvent("M", "Message shown started")
        sgnlWriterE.writerow([time, 'Pause', ' Ends'])
        sgnlWriterE.writerow([time, 'Message = Imaginary', ' Begins'])
        instrMessage()

    if cc==5:
        taskCounter = taskCounter +1
        arrowCounter =  carmenArrowCounter      # Carmen wants it from 60
        mc.sendEvent("M", "Message shown ended")
        mc.sendEvent("ATA", "Arrow task A started")
        sgnlWriterE.writerow([time, 'Message = Imaginary', ' Ends'])
        sgnlWriterE.writerow([time, 'Arrow Task A', ' Begins'])
        # GuiFrame.config(font=("Arial", 20), text='-')
        instrArrows()

    if cc==6:
        mc.sendEvent("ATA", "Arrow task A ended")
        mc.sendEvent("P", "Pause started")
        sgnlWriterE.writerow([time, 'Arrow Task A', ' Ends'])
        sgnlWriterE.writerow([time, 'Pause', ' Begins'])
        instrPause(carmenBtwAndB) # It should be around 120000 = 120 seconds/2 minutes

    if cc==7:
        taskCounter = taskCounter +1
        # GuiFrame.config(font=("Arial", 20), text='-')
        arrowCounter= carmenArrowCounter
        mc.sendEvent("P", "Pause ended")
        mc.sendEvent("ATB", "Arrow task B started")
        sgnlWriterE.writerow([time, 'Pause', ' Ends'])
        sgnlWriterE.writerow([time, 'Arrow Task B', ' Begins'])
        instrArrows()

    if cc==8:
        mc.sendEvent("ATA", "Arrow task B ended")
        mc.sendEvent("P", "Pause started")
        sgnlWriterE.writerow([time, 'Arrow Task B', ' Ends'])
        sgnlWriterE.writerow([time, 'Pause', ' Begins'])
        instrPause(carmenAfterImagin) # It should be 10000 = 10 seconds

    if cc==9:
        mc.sendEvent("P", "Pause ended")
        mc.sendEvent("KYEO", "Keep your eyes open started")
        sgnlWriterE.writerow([time, 'Pause', ' Ends'])
        sgnlWriterE.writerow([time, 'Keep your eyes Open', ' Begins'])
        instrOpenEye()

    if cc==10:
        mc.sendEvent("KYEO", "Keep your eyes open ended")
        mc.sendEvent("TE", "Task Ended")
        sgnlWriterE.writerow([time, 'Keep your eyes open', ' Ends'])
        sgnlWriterE.writerow([time, 'Task', ' Ended'])
        instrThanks()
    if cc == 20:
        sgnlWriterE.writerow([time, ' The task has been canceled by the user'])

def doInstr():
# runs the countdown set the counter for countdown to 0
    global t
    t=0
    lblCount.config(text='')
    lblCount.after(1000,countDown)

def instrOpenEye():
    global taskCounter
    taskCounter = taskCounter + 1
    lblCount.configure(font=("Arial", 40), text=txtEyeOpen)
    if mute == True:
        pygame.mixer.music.load("Sounds\KeepEyeOpen.mp3")
        pygame.mixer.music.play()
    lblCount.after(carmenEyesTask, doInstr)
    
def instrCloseEye():
    global taskCounter
    taskCounter = taskCounter + 1
    lblCount.configure(font=("Arial", 40), text=txtEyeClose)
    if mute == True:
        pygame.mixer.music.load("Sounds\CloseEyes.mp3")
        pygame.mixer.music.play()
    lblCount.after(carmenEyesTask, doInstr)

def instrPause(seconds):
    lblCount.configure(font=("Arial", 40), text='')
    lblCount.after(seconds, doInstr)

def instrMessage():
    lblCount.configure(font=("Arial", 40), text=txtImagin)
    if mute == True:
        pygame.mixer.music.load("Sounds\KeepEyeOpen.mp3") 
        pygame.mixer.music.play()
    lblCount.after(2000,doInstr)

def arrowPause():
    lblCount.configure(text='+', font=("Arial", 280))
    pygame.mixer.music.load("Sounds\SoftBeep2.mp3")
    pygame.mixer.music.play()
    lblCount.after(carmenBtwArrows, instrArrows)

def rand():
# The arrows for the right and left task is chosen randomly
    return random.randint(0,1)

def instrArrows():
    global arrowCounter, sgnlWriterE, taskCounter
    temp = datetime.datetime.now()
    time = str(temp.hour) +':'+ str(temp.minute)+':' + str(temp.second)+':'+str(temp.microsecond)
    temp1 = rand()
    arrow = ''
    if temp1==1:
        arrow='=>'
        sgnlWriterE.writerow([time, "Right"])
    elif temp1==0:
        arrow='<='
        sgnlWriterE.writerow([time, "Left"])
    if arrowCounter>0:
        arrowCounter=arrowCounter-1
        lblCount.configure( text=arrow, font=("Arial", 280), width=2, height=0)
        if arrowCounter == 0:
            lblCount.after(carmenArrowTime, doInstr)
        else:
            lblCount.after(carmenArrowTime, arrowPause)
    
def instrThanks():
    fileWriterEvent.close()
    lblCount.configure(font=("Arial", 40), text=txtTnx)
    if mute==True:
        pygame.mixer.music.load("Sounds\Thanks.mp3")
        pygame.mixer.music.play()
    btnCncl.configure(text='Exit', command=ex)
    erd.setMainConnection()

def setMute():
#sets the mute button to false or true 
    global mute
    if mute == True:
        mute = False
        btnMute.configure(text='-----')
    elif mute == False:
        mute = True
        btnMute.configure(text=txtMute)

def initializeGui():
#Creats and shows the ui
    global root
    root = Tk()
    #Reading the texts from the language file
    readFile = open("TextSettings\ChosenLanguage.txt", "r")
    temp = readFile.readlines()
    temp1 = temp[0]
    chosenLang = open("TextSettings\{}.txt".format(temp1), "r", encoding='utf-8')
    language = chosenLang.readlines()

    global exMessage, txtMute, txtTask, txtEyeOpen, txtEyeClose, txtImagin, txtPaus, txtTnx
    exMessage = language[13].replace('\n', '')
    taskTitle = language[21].replace('\n', '')
    btnCncel = language[6].replace('\n', '')
    btnReady = language[22].replace('\n', '')
    txtMute = language[23].replace('\n', '')
    txtTask = language[24].replace('\n', '')
    txtEyeOpen = language[25].replace('\n', '')
    txtEyeClose = language[26].replace('\n', '')
    txtImagin = language[27].replace('\n', '')
    txtPaus = language[28].replace('\n', '')
    txtTnx = language[29].replace('\n', '')

    #Reading the time from TimeSettings file
    readFile = open("TextSettings\TimeSettings.txt", "r")
    temp = readFile.readlines()
    global carmenCtrl, carmenEyesTask, carmenArrowCounter, carmenB4Imagin, carmenArrowTime
    global carmenBtwArrows, carmenBtwAndB, carmenAfterImagin
    carmenCtrl = int(temp[0].replace('\n', ''))             #Beep between instructions              /2 seconds def
    carmenEyesTask = int(temp[1].replace('\n', ''))         #Close and Open eyes instructions       /2 minutes def
    carmenB4Imagin = int(temp[2].replace('\n', ''))         #Break B4 imagination task              /5 seconds def
    carmenArrowCounter = int(temp[3].replace('\n', ''))     #How many times the arrows shoud run    /60 times def
    carmenArrowTime = int(temp[4].replace('\n', ''))        #How long an arrow should be shown      /3 seconds def
    carmenBtwArrows = int(temp[5].replace('\n', ''))        #Beep between arrows                    /2 seconds def
    carmenBtwAndB = int(temp[6].replace('\n', ''))          #Break between Task A and Task B        /2 minutes def
    carmenAfterImagin =int(temp[7].replace('\n', ''))       #Break after imagination tasks          /10 seconds def
    
    scrnWidth = root.winfo_screenwidth()
    scrnHeight = root.winfo_screenheight()
    root.configure(bg='black')
    global GuiFrame
    GuiFrame = LabelFrame(root, text=taskTitle, bg='black', fg='white')
    GuiFrame.grid(column=0, row=0, padx= scrnWidth/30, pady= scrnHeight/10, ipadx=scrnWidth/2.2, ipady=scrnHeight/2.5)
    GuiFrame.config(font=("Arial", 20))

    btnOk = Button(root, text=btnReady,font=("Arial", 20), bg='black',
        command=lambda:[runThread(), disMute()], borderwidth=8, fg='white')
    btnOk.grid(column=0, row=0)
    global btnCncl
    btnCncl = Button(GuiFrame, text=btnCncel, font=("Arial", 20), 
        command=exGui, bg='black', borderwidth=8, fg='white')
    btnCncl.place(x=scrnWidth/1.3, y=scrnHeight/1.6)
    global btnMute
    btnMute = Button(GuiFrame, command=setMute, font=("Arial", 20), text=txtMute, bg='black', borderwidth=8, fg='white')
    btnMute.place(x=scrnWidth/1.3, y=scrnHeight/5.6)

    root.geometry(f'{scrnWidth}x{scrnHeight}+{-10}+{0}')
    root.attributes("-fullscreen", True)
    root.mainloop()

def main():
    if __name__ == '__main__':
        initializeGui()

def getRooti():
    return root

#Done
