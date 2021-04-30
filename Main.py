#This Class/Script decides if the user have to log in or he is already loged in
#Control if username and password is saved
#It runs LoginGui if the user is not loged in
#Author Rohan

#import csv
from tkinter import *
from tkinter import messagebox, ttk, StringVar
from PIL import ImageTk, Image
import time
import os 
import matplotlib   
import flag
root =Tk()

                    #By clicking on Continue this method will call ConnectToServer 
                    # and sends a user string to the VAS 
def contin():
    import MobiClient as mc 
    us = open("TextSettings\LoginInfo.txt", "r")
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
                    #This method will call Login, by pressing on login button
def login():
    root.destroy()       
    import Login
    Login.initializeGui()

                    #This method will clear the UserInfo text file and let the user to continue to Login
def logout():
    us = open("TextSettings\LoginInfo.txt", "w")
    us.truncate(0)
    us.close()
    btnCont["state"] = "disabled"
    btnLogin["state"] = "normal"
    btnLogout["state"] = "disabled"

                    #This method sets the language to English
def setEng():
    setLanguage("Eng")
    lblEng.configure(bg="blue")
    lblEs.configure(bg="white")
    lblSe.configure(bg="white")
    
                    #This method sets the language to Spanish
def setEs():
    setLanguage("Es")
    lblEs.configure(bg="blue")
    lblEng.configure(bg="white")
    lblSe.configure(bg="white")
    
                    #This method sets the language to Sweish
def setSe():
    setLanguage("Se")
    lblSe.configure(bg="blue")
    lblEs.configure(bg="white")
    lblEng.configure(bg="White")
    
                    #This method writes the chosen language into a textfile
def setLanguage(daLang):
    readfile = open("TextSettings\ChosenLanguage.txt", "w")
    readfile.writelines(daLang)
    readfile.close()
    updateLanguage()
                    #This method updates the words with the chosen language
def updateLanguage():
    global txtWc
    global txtWcTitle
    global txtLogin
    global txtExit
    global txtContin
    global txtLogout

    readFile = open("TextSettings\ChosenLanguage.txt", "r")
    temp = readFile.readlines()
    temp2 = temp[0]
    chosenLang = open("TextSettings\{}.txt".format(temp2), "r", encoding='utf-8')
    temp1= chosenLang.readlines()

    root.title(temp1[0].replace('\n', '') + user)
    lblWel.configure(text= temp1[1] + temp1[2])
    btnLogin.configure(text=temp1[3].replace('\n', ''))
    btnCont.configure(text=temp1[4].replace('\n', ''))
    btnLogout.configure(text=temp1[5].replace('\n', ''))
    btnExit.configure(text=temp1[6].replace('\n', ''))
    readFile.close()
    chosenLang.close()
    
    

                #Creates and runs the interface
def initializeGui():

    global txtWc
    global txtWcTitle
    global txtLogin
    global txtExit
    global txtContin
    global txtLogout
    global lblWel
    global user
    
    readFile = open("TextSettings\ChosenLanguage.txt", "r")
    temp = readFile.readlines()
    temp2 = temp[0]
    chosenLang = open("TextSettings\{}.txt".format(temp2), "r", encoding='utf-8')
    temp1= chosenLang.readlines()
    try:
        readFile1 = open("TextSettings\LoginInfo.txt", "r")
        temp3 = readFile1.readlines()
    except IOError:
        readFile1 = open("TextSettings\LoginInfo.txt", "w")
        readFile1.close()
    
    if os.path.getsize('TextSettings\LoginInfo.txt') < 0:
        user = temp3[0].replace('\n', '')
    else:
        user = ''
    txtWc = (temp1[0].replace('\n', '') + user)
    txtWcTitle = temp1[1] + temp1[2]
    txtLogin = temp1[3].replace('\n', '')
    txtContin = temp1[4].replace('\n', '')
    txtLogout = temp1[5].replace('\n', '')
    txtExit = temp1[6].replace('\n', '')
    readFile.close()
    readFile1.close()
    chosenLang.close()

    root.title(txtWc)
    scrnWidth = root.winfo_screenwidth()
    scrnHeight = root.winfo_screenheight()
    scrnW = root.winfo_reqwidth()
    scrnH = root.winfo_reqheight()
    posR = int(scrnWidth/2 - scrnW)
    posD = int(scrnHeight/2 - scrnH) 

    #Welcome Label
    lblTitel = LabelFrame(root, padx=10, pady=10, border=0)
    lblTitel.grid(column=1, row=0)

    lblWel = Label(lblTitel, text = (txtWcTitle), padx=int(scrnWidth/15), width=int(scrnWidth/60), height=int(scrnHeight/160))
    lblWel.grid(column=0, row=0, sticky="w")
    lblWel.config(font=("Arial", 20))
    lblMT = Label(root, width=int(scrnWidth/100), height=int(scrnHeight/80))
    lblMT.grid(column=0, row=0)

    
        #ButtonFrame for Buttons
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


    
    #Buttons
    global btnCont
    global btnLogin
    global btnLogout
    global btnExit
    
    btnLogin = Button(btnFrame1, text=txtLogin, fg="blue", command=login,  width=int(scrnWidth/80), height=int(scrnHeight/160), borderwidth=2)
    btnLogin.grid(column=0, row=0, sticky="s")
    btnLogin.config(font=("Arial", 14))
    btnCont = Button(btnFrame1, text=txtContin, fg="blue", command=contin, width=int(scrnWidth/80), height=int(scrnHeight/160), borderwidth=2)
    btnCont.grid(column=2, row=0, sticky="w")  
    btnCont.config(font=("Arial", 14))  
    btnLogout = Button(btnFrame1, text=txtLogout, fg="blue", command=logout, width=int(scrnWidth/80), height=int(scrnHeight/160), borderwidth=2)
    btnLogout.grid(column=4, row=0, sticky="w")
    btnLogout.config(font=("Arial", 14))
    btnExit = Button(root, text=txtExit, fg="blue", command=root.destroy, font=46, width=int(scrnWidth/80), height=int(scrnHeight/160), borderwidth=2)
    btnExit.grid(column=1, row=2, sticky="s", pady=10)
    btnExit.config(font=("Arial", 14))
    
    global lblEng
    imageEng = ImageTk.PhotoImage(Image.open("Images\Eng.png"))
    lblEng = Label(langFrame,image=imageEng)# text="hej") # image=imageo)
    if(temp2=="Eng"):
        lblEng = Label(langFrame, bg='blue')
    lblEng.grid(column=0, row=0, sticky="w")
    btnLangEng = Button(lblEng, image=imageEng, command=setEng)
    btnLangEng.grid(column=0, row=0)

    lblF1 = Label(langFrame)
    lblF1.grid(column=1, row=0)
    lblF2 = Label(langFrame)
    lblF2.grid(column=3, row=0)

    global lblEs
    imageEs = ImageTk.PhotoImage(Image.open("Images\Es.png"))
    lblEs = Label(langFrame,image=imageEs)# text="hej") # image=imageo)
    if(temp2=="Es"):
        lblEs = Label(langFrame, bg='blue')
    lblEs.grid(column=2, row=0, sticky="w")
    btnLangEs = Button(lblEs, image=imageEs, command=setEs)
    btnLangEs.grid(column=2, row=0)
    
    global lblSe
    imageSe = ImageTk.PhotoImage(Image.open("Images\Se.png"))
    lblSe = Label(langFrame,image=imageSe)# text="hej") # image=imageo)
    if(temp2=="Se"):
        lblSe = Label(langFrame, bg='blue')
    lblSe.grid(column=4, row=0, sticky="w")
    btnLangSe = Button(lblSe, image=imageSe, command=setSe)
    btnLangSe.grid(column=4, row=0)

    #This option will handle which buttons should be activated and deactivated
    try:
        f = open("TextSettings\LoginInfo.txt", "r")
    except IOError:
        f = open("TextSettings\LoginInfo.txt", "w")
        f.close()
    finally:
        f.close()
    with open("TextSettings\LoginInfo.txt", "r") as f:
        if os.path.getsize('TextSettings\LoginInfo.txt') > 0:
            btnCont["state"] = "normal"
            btnLogin["state"] = "disabled"
        else :
            btnCont["state"] = "disabled"
            btnLogin["state"] = "normal"
            btnLogout["state"] = "disabled"

   

        #Decides the size of the screen 
    root.geometry(f'{posR*2}x{posD*3}+{posR-300}+{posD-int(posD/2)}')
    root.attributes("-fullscreen", False)
    root.mainloop()




initializeGui()





















