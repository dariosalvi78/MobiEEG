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
import ConnToCap as coca 

fileWriter =''

t=3
counter = 0
pygame.init()
pygame.mixer.init()
mute = True
taskCounter = 0
arrowCounter = 10

def exGui():
    response = messagebox.askyesno(message=exMessage)
    if response == 1:
        mc.sendEvent("TC", "The task has been canceled by the user")
        checkInst(20)
        ex()
        
def ex():
    coca.exitFromInstruction()
    root.destroy()

def disMute():
    global btnMute
    btnMute.destroy()
    coca.setSendTrue()
    mc.setTime()


def countDown():
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
            # Carmen watns to have controll over the time of the Cross
            lblCount.after(carmenCtrl, countDown)
        
    elif t==-1:
        counter = counter + 1
        checkInst(counter)

def instWriter(fWriterE):
    global fileWriterEvent
    fileWriterEvent = fWriterE
    

def checkInst(cc):
    global arrowCounter
    global taskCounter
    global mc
    temp = datetime.datetime.now()
    time = str(temp.hour) +':'+ str(temp.minute)+':' + str(temp.second)+':'+str(temp.microsecond)
    sgnlWriterE = csv.writer(fileWriterEvent, delimiter=',', quotechar='"', 
    quoting=csv.QUOTE_MINIMAL)


    if cc==1:
        mc.sendEvent("KYEO", "Keep your eyes open started")
        sgnlWriterE.writerow(['Time='+time, 'Keep your eyes open', ' Begins'])
        instrOpenEye()

    if cc==2:
        mc.sendEvent("KYEO", "Keep your eyes open ended")
        mc.sendEvent("KYEC", "Keep your eyes closed started")
        sgnlWriterE.writerow(['Time='+time, 'Keep your eyes open', ' Ends'])
        sgnlWriterE.writerow(['Time='+time, 'Keep your eyes closed', ' Begins'])
        instrCloseEye()

    if cc==3:
        mc.sendEvent("KYEc", "Keep your eyes closed ended")
        mc.sendEvent("P", "Pause started")
        sgnlWriterE.writerow(['Time='+time, 'Keep your eyes closed', ' Ends'])
        sgnlWriterE.writerow(['Time='+time, 'Pause', ' Begins'])
        instrPause(carmenB4Imagin) # It should be 3000 = 3 seconds

    if cc==4:
        mc.sendEvent("P", "Pause ended")
        mc.sendEvent("M", "Message shown started")
        sgnlWriterE.writerow(['Time='+time, 'Pause', ' Ends'])
        sgnlWriterE.writerow(['Time='+time, 'Message = Imaginary', ' Begins'])
        instrMessage()

    if cc==5:
        taskCounter = taskCounter +1
        arrowCounter =  carmenArrowCounter      # Carmen wants it from 60
        mc.sendEvent("M", "Message shown ended")
        mc.sendEvent("ATA", "Arrow task A started")
        sgnlWriterE.writerow(['Time='+time, 'Message = Imaginary', ' Ends'])
        sgnlWriterE.writerow(['Time='+time, 'Arrow Task A', ' Begins'])
        # GuiFrame.config(font=("Arial", 20), text='-')
        instrArrows()

    if cc==6:
        mc.sendEvent("ATA", "Arrow task A ended")
        mc.sendEvent("P", "Pause started")
        sgnlWriterE.writerow(['Time='+time, 'Arrow Task A', ' Ends'])
        sgnlWriterE.writerow(['Time='+time, 'Pause', ' Begins'])
        instrPause(carmenBtwAndB) # It should be around 120000 = 120 seconds/2 minutes
        

    if cc==7:
        taskCounter = taskCounter +1
        # GuiFrame.config(font=("Arial", 20), text='-')
        arrowCounter= carmenArrowCounter
        mc.sendEvent("P", "Pause ended")
        mc.sendEvent("ATB", "Arrow task B started")
        sgnlWriterE.writerow(['Time='+time, 'Pause', ' Ends'])
        sgnlWriterE.writerow(['Time='+time, 'Arrow Task B', ' Begins'])
        instrArrows()

    if cc==8:
        mc.sendEvent("ATA", "Arrow task B ended")
        mc.sendEvent("P", "Pause started")
        sgnlWriterE.writerow(['Time='+time, 'Arrow Task B', ' Ends'])
        sgnlWriterE.writerow(['Time='+time, 'Pause', ' Begins'])
        instrPause(carmenAfterImagin) # It should be 10000 = 10 seconds

    if cc==9:
        mc.sendEvent("P", "Pause ended")
        mc.sendEvent("KYEO", "Keep your eyes open started")
        sgnlWriterE.writerow(['Time='+time, 'Pause', ' Ends'])
        sgnlWriterE.writerow(['Time='+time, 'Keep your eyes Open', ' Begins'])
        instrOpenEye()

    if cc==10:
        mc.sendEvent("KYEO", "Keep your eyes open ended")
        mc.sendEvent("TE", "Task Ended")
        sgnlWriterE.writerow(['Time='+time, 'Keep your eyes open', ' Ends'])
        sgnlWriterE.writerow(['Time='+time, 'Task', ' Ended'])
        coca.closeDataFile()
        # mc.StopSendDataToServer()
        print(datetime.datetime.now())
        instrThanks()
    if cc == 20:
        sgnlWriterE.writerow(['Time='+time, 'TC', ' The task has been canceled by the user'])

        


def doInstr():
    global t
    t=0
    # GuiFrame.configure(bg='black', text='-')
    lblCount.config(text='')
    lblCount.after(1000,countDown)

def instrOpenEye():
    global taskCounter
    taskCounter = taskCounter + 1
    # GuiFrame.config(font=("Arial", 20), text='-')
    lblCount.configure(font=("Arial", 40), text=txtEyeOpen)
    if mute == True:
        pygame.mixer.music.load("Sounds\KeepEyeOpen.mp3")
        pygame.mixer.music.play()
    lblCount.after(carmenEyesTask, doInstr)
    
def instrCloseEye():
    global taskCounter
    taskCounter = taskCounter + 1
    # GuiFrame.config(font=("Arial", 20), text='-')
    lblCount.configure(font=("Arial", 40), text=txtEyeClose)
    if mute == True:
        pygame.mixer.music.load("Sounds\CloseEyes.mp3")
        pygame.mixer.music.play()
    lblCount.after(carmenEyesTask, doInstr)

def instrPause(seconds):
    # GuiFrame.config(font=("Arial", 20), text='-')
    lblCount.configure(font=("Arial", 40), text='')
    lblCount.after(seconds, doInstr)

def instrMessage():
    # GuiFrame.config(font=("Arial", 20), text='-')
    lblCount.configure(font=("Arial", 40), text=txtImagin)
    if mute == True:
        pygame.mixer.music.load("Sounds\KeepEyeOpen.mp3") # should change
        pygame.mixer.music.play()
    lblCount.after(2000,doInstr)

def arrowPause():
    lblCount.configure(text='+', font=("Arial", 280))
    pygame.mixer.music.load("Sounds\SoftBeep2.mp3")
    pygame.mixer.music.play()
    lblCount.after(carmenBtwArrows, instrArrows)

def rand():
    return random.randint(0,1)

def instrArrows():
    global arrowCounter
    global taskCounter
    # image = Image.open("Images\Eng.png")
    # bgImage = ImageTk.PhotoImage(image)
    temp = rand()
    arrow = ''
    if temp==1:
        arrow='=>'
    elif temp==0:
        arrow='<='
    
    if arrowCounter>0:
        arrowCounter=arrowCounter-1
        lblCount.configure( text=arrow, font=("Arial", 280), width=2, height=0)
        if arrowCounter == 0:
            lblCount.after(carmenArrowTime, doInstr)
        else:
            lblCount.after(carmenArrowTime, arrowPause)
    
def instrThanks():
    # GuiFrame.config(font=("Arial", 20), text='-')
    fileWriterEvent.close()
    lblCount.configure(font=("Arial", 40), text=txtTnx)
    if mute==True:
        pygame.mixer.music.load("Sounds\Thanks.mp3")
        pygame.mixer.music.play()
    btnCncl.configure(text='Exit', command=ex)
    

def setMute():
    global mute
    if mute == True:
        mute = False
        btnMute.configure(text='-----')
    elif mute == False:
        mute = True
        btnMute.configure(text=txtMute)

def initializeGui():
    global root
    root = Tk()
    #Reading the texts from the language file
    readFile = open("TextSettings\ChosenLanguage.txt", "r")
    temp = readFile.readlines()
    temp1 = temp[0]
    chosenLang = open("TextSettings\{}.txt".format(temp1), "r", encoding='utf-8')
    language = chosenLang.readlines()
    global exMessage
    global txtMute
    global txtTask
    global txtEyeOpen
    global txtEyeClose
    global txtImagin
    global txtPaus
    global txtTnx
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
    global carmenCtrl
    global carmenEyesTask
    global carmenArrowCounter
    global carmenB4Imagin
    global carmenArrowTime
    global carmenBtwArrows
    global carmenBtwAndB
    global carmenAfterImagin
    carmenCtrl = int(temp[0].replace('\n', ''))             #Beep between instructions              /2 seconds def
    carmenEyesTask = int(temp[1].replace('\n', ''))         #Close and Open eyes instructions       /2 minutes def
    carmenB4Imagin = int(temp[2].replace('\n', ''))       #Break B4 imagination task              /5 seconds def
    carmenArrowCounter = int(temp[3].replace('\n', ''))     #How many times the arrows shoud run    /60 times def
    carmenArrowTime = int(temp[4].replace('\n', ''))        #How long an arrow should be shown      /3 seconds def
    carmenBtwArrows = int(temp[5].replace('\n', ''))        #Beep between arrows                    /2 seconds def
    carmenBtwAndB = int(temp[6].replace('\n', ''))           #Break between Task A and Task B        /2 minutes def
    carmenAfterImagin =int(temp[7].replace('\n', ''))       #Break after imagination tasks          /10 seconds def
    
    scrnWidth = root.winfo_screenwidth()
    scrnHeight = root.winfo_screenheight()
    root.configure(bg='black')
    global GuiFrame
    GuiFrame = LabelFrame(root, text=taskTitle, bg='black', fg='white')
    GuiFrame.grid(column=0, row=0, padx= scrnWidth/30, pady= scrnHeight/10, ipadx=scrnWidth/2.2, ipady=scrnHeight/2.5)
    GuiFrame.config(font=("Arial", 20))

    btnOk = Button(root, text=btnReady,font=("Arial", 20), bg='black',
        command=lambda:[countDown(), disMute()], borderwidth=8, fg='white')
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




main()
