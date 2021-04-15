#This scene is the scene number2 which allows the user to choose the level of pain. Visual Scale Analogue.
#It will be between 0 and 10
#This scene includes Analogue/Digital level alternative and three buttons: Continue, Log out and Cancel
#Author Rohan

from tkinter import *
import datetime
import os
user = ''
                #Recieves a string and sets the username to it
def setUserName(userName):
    global user
    user = userName

                #Stores the pain level and the time of the test in a textfile
def confirm():
    # if os.path.isfile("Report\{}.txt".format(user)):
    #     report = open("Report\{}.txt".format(user), "a")
    #     report.writelines("Date and Time: " + str(datetime.datetime.now()) + "\n")
    #     report.writelines("Pain level: " + str(horizont.get()) + "\n")
    #     report.close()
    # else:
    #     report = open("Report\{}.txt".format(user), "w")
    #     report.writelines("Date and Time: " + str(datetime.datetime.now()) + "\n")
    #     report.writelines("Pain level: " + str(horizont.get()) + "\n")
    #     report.close()
    # try:
    #     f = open("Report\{}.txt".format(user), "r")
    # except IOError:
    #     f = open("Report\{}.txt".format(user), "w")
    #     f.close()
    # finally:
    #     close()

   
    
    import ConnToCap as cc 
    import MobiClient as mc
    mc.SendPainLevel(horizont.get())
    cc.setVAS(horizont.get())
    cc.setUserName(user)
    cc.updateGui(root)

                # Popup message for confirming if the user really wants to exit
def exGui():
    response = messagebox.askyesno(message="Are you sure you want to exit?")
    if response == 1:
        root.destroy()

                # Creates and shows the GUI
def initializeGui():

    readFile = open("TextSettings\ChosenLanguage.txt", "r")
    temp = readFile.readlines()
    temp1 = temp[0]
    chosenLang = open("TextSettings\{}.txt".format(temp1), "r", encoding='utf-8')
    language = chosenLang.readlines()

    barTitle = language[16].replace('\n', '')
    frTitle = language[17].replace('\n', '')
    conf = language[18].replace('\n', '')

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
    root.mainloop()

def main():
    if __name__ == '__main__':
        initializeGui()

main()