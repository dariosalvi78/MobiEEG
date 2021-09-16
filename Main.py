'''
The main script to run the program
The Main GUI runs and the user should choose either he wants to continue 
with previous stored account or log out and login with another account. 
@uthor Rohan Samandari
'''

import Settings
from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()


def contin():
    # Continues to log in with previous inlogged account

    import MobiClient as mc
    us = open("settings/LoginInfo.txt", "r")
    temp = us.readlines()
    userID = temp[0].replace('\n', '')
    passW = temp[1].replace('\n', '')
    connection = mc.logIn(userID, passW)
    if(connection == True):
        import ConnectToCap as cs
        import VAS
        VAS.setUserName(userID)
        us.close()
        root.destroy()
        cs.initializeGui()
    else:
        root.destroy()
        import Login
        Login.initializeGui()


def login():
    # Runs Login Gui
    root.destroy()
    import Login
    Login.initializeGui()


def logout():
    # Clear the UserInfo text file and let the user to continue to Login

    us = open("settings/LoginInfo.txt", "w")
    us.truncate(0)
    us.close()
    btnCont["state"] = "disabled"
    btnLogin["state"] = "normal"
    btnLogout["state"] = "disabled"


def setEng():
    # This method sets the language to English

    setLanguage("en")
    lblEng.configure(bg="blue")
    lblEs.configure(bg="white")
    lblSe.configure(bg="white")


def setEs():
    # This method sets the language to Spanish
    setLanguage("es")
    lblEs.configure(bg="blue")
    lblEng.configure(bg="white")
    lblSe.configure(bg="white")


def setSe():
    # This method sets the language to Sweish
    setLanguage("se")
    lblSe.configure(bg="blue")
    lblEs.configure(bg="white")
    lblEng.configure(bg="White")


def setLanguage(daLang):
    # This method writes the chosen language into a textfile
    Settings.settings['language'] = daLang
    Settings.saveSettings()
    updateLanguage()


def updateLanguage():
    # This method updates the labels with the chosen language words

    global txtWc
    global txtWcTitle
    global txtLogin
    global txtExit
    global txtContin
    global txtLogout

    chosenLang = open("i18n/{}.txt".format(
        Settings.settings['language']), "r", encoding='utf-8')
    temp1 = chosenLang.readlines()

    root.title(temp1[0].replace('\n', '') + user)
    lblWel.configure(text=temp1[1] + temp1[2])
    btnLogin.configure(text=temp1[3].replace('\n', ''))
    btnCont.configure(text=temp1[4].replace('\n', ''))
    btnLogout.configure(text=temp1[5].replace('\n', ''))
    btnExit.configure(text=temp1[6].replace('\n', ''))
    chosenLang.close()


def initializeGui():
    # open settins
    Settings.loadSettings()
    # Creates and runs the interface

    global txtWc
    global txtWcTitle
    global txtLogin
    global txtExit
    global txtContin
    global txtLogout
    global lblWel
    global user

    print(Settings.settings)
    chosenLang = open("i18n/{}.txt".format(
        Settings.settings['language']), "r", encoding='utf-8')
    temp1 = chosenLang.readlines()
    try:
        readFile1 = open("settings/LoginInfo.txt", "r")
        temp3 = readFile1.readlines()
    except IOError:
        readFile1 = open("settings/LoginInfo.txt", "w")
        readFile1.close()

    if os.path.getsize('settings/LoginInfo.txt') < 0:
        user = temp3[0].replace('\n', '')
    else:
        user = ''
    txtWc = (temp1[0].replace('\n', '') + user)
    txtWcTitle = temp1[1] + temp1[2]
    txtLogin = temp1[3].replace('\n', '')
    txtContin = temp1[4].replace('\n', '')
    txtLogout = temp1[5].replace('\n', '')
    txtExit = temp1[6].replace('\n', '')
    readFile1.close()
    chosenLang.close()

    root.title(txtWc)
    scrnWidth = root.winfo_screenwidth()
    scrnHeight = root.winfo_screenheight()
    scrnW = root.winfo_reqwidth()
    scrnH = root.winfo_reqheight()
    posR = int(scrnWidth/2 - scrnW)
    posD = int(scrnHeight/2 - scrnH)

    # Welcome Label
    lblTitel = LabelFrame(root, padx=10, pady=10, border=0)
    lblTitel.grid(column=1, row=0)

    lblWel = Label(lblTitel, text=(txtWcTitle), padx=int(
        scrnWidth/15), width=int(scrnWidth/60), height=int(scrnHeight/160))
    lblWel.grid(column=0, row=0, sticky="w")
    lblWel.config(font=("Arial", 20))
    lblMT = Label(root, width=int(scrnWidth/100), height=int(scrnHeight/80))
    lblMT.grid(column=0, row=0)

    # ButtonFrame for Buttons
    btnFrame1 = LabelFrame(root, padx=10, pady=10)
    btnFrame1.grid(column=1, row=1)
    btnFrame2 = LabelFrame(root, padx=10, pady=10)
    btnFrame2.grid(column=1, row=2)
    lblMT1 = Label(btnFrame1, width=5)
    lblMT1.grid(column=1, row=0)
    lblMT2 = Label(btnFrame1, width=5)
    lblMT2.grid(column=3, row=0)
    langFrame = LabelFrame(lblTitel, borderwidth=0)
    langFrame.grid(column=1, row=0)

    # Buttons
    global btnCont
    global btnLogin
    global btnLogout
    global btnExit

    btnLogin = Button(btnFrame1, text=txtLogin, fg="blue", command=login,  width=int(
        scrnWidth/80), height=int(scrnHeight/160), borderwidth=2)
    btnLogin.grid(column=0, row=0, sticky="s")
    btnLogin.config(font=("Arial", 14))
    btnCont = Button(btnFrame1, text=txtContin, fg="blue", command=contin, width=int(
        scrnWidth/80), height=int(scrnHeight/160), borderwidth=2)
    btnCont.grid(column=2, row=0, sticky="w")
    btnCont.config(font=("Arial", 14))
    btnLogout = Button(btnFrame1, text=txtLogout, fg="blue", command=logout, width=int(
        scrnWidth/80), height=int(scrnHeight/160), borderwidth=2)
    btnLogout.grid(column=4, row=0, sticky="w")
    btnLogout.config(font=("Arial", 14))
    btnExit = Button(root, text=txtExit, fg="blue", command=root.destroy, font=46, width=int(
        scrnWidth/80), height=int(scrnHeight/160), borderwidth=2)
    btnExit.grid(column=1, row=2, sticky="s", pady=10)
    btnExit.config(font=("Arial", 14))

    global lblEng
    imageEng = ImageTk.PhotoImage(Image.open("Images/Eng.png"))
    lblEng = Label(langFrame, image=imageEng)  # text="hej") # image=imageo)
    if(Settings.settings['language'] == "en"):
        lblEng = Label(langFrame, bg='blue')
    lblEng.grid(column=0, row=0, sticky="w")
    btnLangEng = Button(lblEng, image=imageEng, command=setEng)
    btnLangEng.grid(column=0, row=0)

    lblF1 = Label(langFrame)
    lblF1.grid(column=1, row=0)
    lblF2 = Label(langFrame)
    lblF2.grid(column=3, row=0)

    global lblEs
    imageEs = ImageTk.PhotoImage(Image.open("Images/Es.png"))
    lblEs = Label(langFrame, image=imageEs)  # text="hej") # image=imageo)
    if(Settings.settings['language'] == "es"):
        lblEs = Label(langFrame, bg='blue')
    lblEs.grid(column=2, row=0, sticky="w")
    btnLangEs = Button(lblEs, image=imageEs, command=setEs)
    btnLangEs.grid(column=2, row=0)

    global lblSe
    imageSe = ImageTk.PhotoImage(Image.open("Images/Se.png"))
    lblSe = Label(langFrame, image=imageSe)  # text="hej") # image=imageo)
    if(Settings.settings['language'] == "se"):
        lblSe = Label(langFrame, bg='blue')
    lblSe.grid(column=4, row=0, sticky="w")
    btnLangSe = Button(lblSe, image=imageSe, command=setSe)
    btnLangSe.grid(column=4, row=0)

    # This option will handle which buttons should be activated and deactivated
    try:
        f = open("settings/LoginInfo.txt", "r")
    except IOError:
        f = open("settings/LoginInfo.txt", "w")
        f.close()
    finally:
        f.close()
    with open("settings/LoginInfo.txt", "r") as f:
        if os.path.getsize('settings/LoginInfo.txt') > 0:
            btnCont["state"] = "normal"
            btnLogin["state"] = "disabled"
        else:
            btnCont["state"] = "disabled"
            btnLogin["state"] = "normal"
            btnLogout["state"] = "disabled"

    # Decides the size of the screen
    root.geometry(f'{posR*2}x{posD*3}+{posR-300}+{posD-int(posD/2)}')
    root.attributes("-fullscreen", False)
    root.mainloop()


initializeGui()

# Done
