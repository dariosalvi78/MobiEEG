# This wait page is only going to be shown while the application is connecting to the server
# Author: Rohan
 
from tkinter import *
import tkinter
import EEGReadData as erd
from tkinter import messagebox
from multiprocessing import Process
import threading
import time
import sys
root =Tk()
user = None
dotAnim = 5
messConn = "Connecting"
again = False


def exit():
    global root
    root.destroy()
    # erd.setMainConnection()
    # response = messagebox.askyesno(message="Bye")
    # if response == 1:
    #     root.destroy()
    # else:
    #     erd.setMainConnectionTrue()
    #     root.after(1000, runThread)


def runThread():

    global lblText, again, btnExit, btnConnect
    btnExit['state'] = "disabled"
    btnConnect['state'] = "disabled"
    messConn="Connecting"
    lblText.config(text=messConn)
    t1 = threading.Thread(target=erd.connectToEEG)
    t2 = threading.Thread(target=connectToCap)
    t1.start()
    t2.start()

def connectToCap():
    global cond, dotAnim, lblText, messConn, root, btnExit, btnConnect
    cond = erd.capConnected()
    lblText.config(text='')
    if(cond == False):
        if(dotAnim == 0):
            messCon = "Unable to connect\nTurn on the EEG device"
            lblText.config(text=messCon)
            dotAnim = 5
            btnExit['state'] = "active"
            btnConnect["state"] = "active"
        else:
            messConn += "." 
            lblText.config(text=messConn)
            dotAnim -=1
            root.after(1000, connectToCap)

    else:
        messCon = "The Device is connected"
        lblText.config(text=messCon)
        root.after(3000, close)

def close():
    import VAS
    root.destroy()
    # erd.readData()
    # threading.Thread(target=erd.readData).start()
    VAS.initializeGui()


def initializeGui():

    readFile = open("TextSettings\ChosenLanguage.txt", "r")
    temp = readFile.readlines()
    temp1 = temp[0]
    chosenLang = open("TextSettings\{}.txt".format(temp1), "r", encoding='utf-8')
    language = chosenLang.readlines()
    barTitle = language[14].replace('\n', '')
    frTitle = language[15].replace('\n', '')
    readFile.close()
    chosenLang.close()

    root.title(barTitle)
    scrnWidth = root.winfo_screenwidth()
    scrnHeight = root.winfo_screenheight()
    scrnW = root.winfo_reqwidth()
    scrnH = root.winfo_reqheight()
    posR = int(scrnWidth/2 - scrnW)
    posD = int(scrnHeight/2 - scrnH) 

    global lblText
    lblTitel = LabelFrame(root,width=int(scrnWidth/2), height=int(scrnHeight/4),padx=10,  pady=10, border=0)# padx=scrnWidth/7, width=int(scrnWidth/2), height=int(scrnHeight/2), pady=10, border=1)
    lblTitel.config(font=("Arial", 20))
    lblTitel.grid_propagate(False)
    lblTitel.grid(column=0, row=0)
    lblText = Label(lblTitel, text="Turn on the EEG device\n\nConnecting to the EEG Device")
    lblText.config(font=("Arial", 20))
    lblText.grid(column=0, row=0)

    global btnExit, btnConnect
    btnExit = Button(root, text="Exit", command=exit)
    btnExit.configure(font=("Arial", 20))
    btnExit.grid(column=1, row=1)

    btnConnect = Button(root, text="Try again", command=runThread)
    btnConnect.configure(font=("Arial", 20))
    btnConnect.grid(column=0, row=1)
    btnExit['state'] = "disabled"
    btnConnect['state'] = "disabled"
    

        #Decides the size of the screen 
    root.geometry(f'{800}x{300}+{posR-200}+{posD}')
    root.after(500, runThread)
    root.attributes("-fullscreen", False)
    root.mainloop()


def main():
    if __name__ == '__main__':
        initializeGui()
    
main()