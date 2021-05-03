'''
The Visual Scale Analogue VAS lets the user to choose a level of pain. 
The painlevel is then send to the MobiClient for to be send to the server
@uthor Rohan
'''

from tkinter import *

user = ''
def setUserName(userName):
#Recieves a string and sets the username to it
    global user
    user = userName

                
def confirm():
#Stores and sends the pain level and the time of the test in a textfile

    import SignalGui as cc 
    import MobiClient as mc
    import EEGToCSV as ecs

    mc.SendPainLevel(horizont.get())
    ecs.setVAS(horizont.get())
    cc.setUserName(user)
    cc.updateGui(root)

                
def exGui():
# Popup message for confirming if the user wants to exit
    global mess
    response = messagebox.askyesno(message=mess)
    if response == 1:
        root.destroy()

                
def initializeGui():
# Creates and shows the GUI

    readFile = open("TextSettings\ChosenLanguage.txt", "r")
    temp = readFile.readlines()
    temp1 = temp[0]
    chosenLang = open("TextSettings\{}.txt".format(temp1), "r", encoding='utf-8')
    language = chosenLang.readlines()

    barTitle = language[16].replace('\n', '')
    frTitle = language[17].replace('\n', '')
    conf = language[18].replace('\n', '')
    global mess 
    mess = language[13].replace('\n', '')

    global root
    root =Tk()
    root.title(barTitle + user)
    scrnWidth = root.winfo_screenwidth()
    scrnHeight = root.winfo_screenheight()

    GuiFrame = LabelFrame(root, text=frTitle +user, padx=scrnWidth/10, pady=scrnHeight/20)
    GuiFrame.grid(column=0, row=0, padx=scrnWidth/19, pady= scrnHeight/8, ipadx=scrnWidth/320, ipady=scrnHeight/19)
    GuiFrame.config(font=("Arial", 20))

    global horizont
    horizont = Scale(GuiFrame, from_=0, to=10, orient=HORIZONTAL, width=scrnWidth/25,resolution=0.1, bd=2, digits=3, showvalue=False,
    font=("Arial", 25), length=scrnWidth/1.5, relief="groove", sliderlength=50, tickinterval=10)
    horizont.grid(column=0, row=0)
    
    #EmptyLabel
    lblMT = Label(GuiFrame, height=int(scrnHeight/100))
    lblMT.grid(column=2, row=1)

    #Button
    btnCon = Button(GuiFrame, text=conf, command=confirm, fg="blue")
    btnCon.grid(column=0, row=2, sticky="e")
    btnCon.config(font=("Arial", 18))

    #Decides the size of the screen
    root.geometry(f'{scrnWidth}x{scrnHeight}+{-10}+{0}')
    root.attributes("-fullscreen", True)
    root.lift()
    root.mainloop()

def main():
    if __name__ == '__main__':
        initializeGui()

#Done