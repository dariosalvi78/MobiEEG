'''
Connecting to the EEG device by help from EEGReadData. The Gui is shown and after connecting two threads will run
@uthor Rohan Samandari
'''

import Settings
from tkinter import *
import tkinter
import EEGReadData as erd
import threading
root = Tk()
user = None
dotAnim = 5
messConn = ""


def exit():
    global root
    root.destroy()


def runThread():
    # Runs the connection and reading data from EEG device with help of EEGReadData as a new thread
    # and runs a seperate GUI with another thread

    global lblText, btnExit, btnConnect, messConn
    btnExit['state'] = "disabled"
    btnConnect['state'] = "disabled"

    lblText.config(text=messConn)
    t1 = threading.Thread(target=erd.connectToEEG)
    # t2 = threading.Thread(target=connectToCap)
    t1.start()
    connectToCap()
    # t2.start()


def connectToCap():
    # Receives a bool value from EEGReadData and if its True the next method will run VAS gui

    global cond, dotAnim, lblText, messConn, root, btnExit, btnConnect, lblMess3
    global lblMess4, lblConnected
    cond = erd.capConnected()
    lblText.config(text='')
    if(cond == False):
        if(dotAnim == 0):
            messCon = lblMess3 + lblMess4
            lblText.config(text=messCon)
            dotAnim = 5
            btnExit['state'] = "active"
            btnConnect["state"] = "active"
        else:
            messConn += "."
            lblText.config(text=messConn)
            dotAnim -= 1
            root.after(1000, connectToCap)

    else:
        messCon = lblConnected
        lblText.config(text=messCon)
        root.after(3000, close)


def close():
    # Will close the gui and run next gui
    import VAS
    root.destroy()
    VAS.initializeGui()


def initializeGui():
    # Creates and shows the GUI
    chosenLang = open(
        "i18n/{}.txt".format(Settings.settings['language']), "r", encoding='utf-8')
    language = chosenLang.readlines()
# Setts the chosen language
    barTitle = language[14].replace('\n', '')
    frTitle = language[15].replace('\n', '')
    lblMess = language[32]
    lblMess2 = language[33].replace('\n', '')
    btnTry = language[34].replace('\n', '')
    txtExit = language[6].replace('\n', '')
    global lblMess3, lblMess4, lblConnected, messConn
    lblMess3 = language[35]
    lblMess4 = language[36].replace('\n', '')
    lblConnected = language[37].replace('\n', '')
    messConn = language[38].replace('\n', '')

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
    # padx=scrnWidth/7, width=int(scrnWidth/2), height=int(scrnHeight/2), pady=10, border=1)
    lblTitel = LabelFrame(root, width=int(scrnWidth/2),
                          height=int(scrnHeight/4), padx=10,  pady=10, border=0)
    lblTitel.config(font=("Arial", 20))
    lblTitel.grid_propagate(False)
    lblTitel.grid(column=0, row=0)
    lblText = Label(lblTitel, text=lblMess + lblMess2)
    lblText.config(font=("Arial", 20))
    lblText.grid(column=0, row=0)

    global btnExit, btnConnect
    btnExit = Button(root, text=txtExit, command=exit)
    btnExit.configure(font=("Arial", 20))
    btnExit.grid(column=1, row=1)

    btnConnect = Button(root, text=btnTry, command=runThread)
    btnConnect.configure(font=("Arial", 20))
    btnConnect.grid(column=0, row=1)
    btnExit['state'] = "disabled"
    btnConnect['state'] = "disabled"

    # Decides the size of the screen
    root.geometry(f'{800}x{300}+{posR-200}+{posD}')
    root.after(500, runThread)
    root.attributes("-fullscreen", False)
    root.mainloop()


def main():
    if __name__ == '__main__':
        initializeGui()
# Done
