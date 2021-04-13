#An application written by Rohan Samandari
#The first scene which is about loging in in a Mobistudy server. 
#This scene contains two inputbox for email and password, and two buttons. Log in logs the user in and Sign up will 
# take the user to the Mobistudy webapplication. 
#Author Rohan

from tkinter import *

import os
import time
import keyboard
from tkinter import messagebox
root = Tk() 

    #By clikcing on LoginBtn the next screen should run and this screen should close
def clickLog():
    readfile = open("TextSettings\LoginInfo.txt", "w")
    readfile.writelines([inpMail.get(), "\n" ,inpPass.get()])
    readfile.close()
    temp = open("TextSettings\LoginInfo.txt", "r")
    temp1 = temp.readlines()
    temp2 = temp1[0].replace('\n', '')
    temp3 = temp1[1].replace('\n', '')

# Logging in to the server
    import MobiClient as mc 
    connection = mc.logIn(temp2, temp3)
    if(connection== True):
        import VAS
        import ConnectToServer
        VAS.setUserName(temp2)
        temp.close()
        root.destroy()
        ConnectToServer.initializeGui()
    elif(connection == False):
        response = messagebox.showwarning(message=exMessage)
        if response == 1:
            import ConnToCap
            ConnToCap.exitFromInstruction()
            root.destroy()
        
    

                #Clears the input box
def clearMail(event):
    inpMail.delete(0, 'end')
    return None

                #Clears the input box
def clearPass(event):
    inpPass.delete(0, "end")
    return None

                    # Popup message for confirming if the user really wants to exit
def exGui():
    
    response = messagebox.askyesno(message=txtMess)
    if response == 1:
        root.destroy()

    # Creates the GUI
def initializeGui():

    readFile = open("TextSettings\ChosenLanguage.txt", "r")
    temp = readFile.readlines()
    temp1 = temp[0]
    chosenLang = open("TextSettings\{}.txt".format(temp1), "r", encoding='utf-8')
    language = chosenLang.readlines()

    barTitle = language[7].replace('\n', '')
    frTitle = language[8].replace('\n', '')
    email = language[9].replace('\n', '')
    em = language[10].replace('\n', '')
    password = language[11].replace('\n', '')
    passw = language[12].replace('\n', '')
    login = language[3].replace('\n', '')
    ex = language[6].replace('\n', '')
    global txtMess
    txtMess = language[13].replace('\n', '')
    global exMessage
    exMessage = language[30].replace('\n', '')
    readFile.close()
    chosenLang.close()

    root.title(barTitle)
    scrnWidth = root.winfo_screenwidth()
    scrnHeight = root.winfo_screenheight()
    scrnW = root.winfo_reqwidth()
    scrnH = root.winfo_reqheight()
    posR = int(scrnWidth/2 - scrnW)
    posD = int(scrnHeight/2 - scrnH) 
    
    GuiFrame = LabelFrame(root, text=frTitle, padx=scrnWidth/160, pady=scrnHeight/30)
    GuiFrame.config(font=("arial", 25))
    GuiFrame.grid(column=0, row=0, padx=scrnWidth/12, pady= scrnHeight/8, ipadx=scrnWidth/30, sticky="s")
    btnFrame = LabelFrame(GuiFrame, borderwidth=0)
    btnFrame.grid(column=2, row=5, sticky="s")
   
                #Label and Input field for mailaddress 
    global inpMail
    global inpPass
    inpMail = Entry(GuiFrame, width=int(scrnWidth/30), borderwidth=2, fg="gray")
    inpMail.grid(row=1, column=2, sticky=N)
    inpMail.insert(0, em)
    inpMail.bind("<Button-1>", clearMail)
    inpMail.config(font=("Arial", 20))
    lblMail = Label(GuiFrame, text=email)
    lblMail.config(font=("Arial", 24))
    lblMail.grid(row=1, column=1, sticky=W)
                #Label and Input field for password
    inpPass = Entry(GuiFrame, width=int(scrnWidth/30), borderwidth=2, show="*", fg="gray")
    inpPass.config(font=("Arial", 20))
    inpPass.grid(column=2, row=3, sticky=W)
    lblPass = Label(GuiFrame, text=password)
    lblPass.config(font=("Arial", 24))
    lblPass.grid(row=3, column=1, sticky=W)
    inpPass.insert(0, passw)
    inpPass.bind("<Button-1>", clearPass) 

    lblSpace = Label(GuiFrame, height=int(scrnHeight/150))
    lblSpace.grid(row=0)
    lblSpace2 = Label(GuiFrame, width=int(scrnWidth/100))
    lblSpace2.grid(column=0)
    lblBtwField = Label(GuiFrame, height=int(scrnHeight/300))
    lblBtwField.grid(row=2)
    lblBtwFrame = Label(GuiFrame, height=int(scrnHeight/100))
    lblBtwFrame.grid(row=4)
    lblBtwBtns = Label(GuiFrame, height=int(scrnHeight/160))
    lblBtwBtns.grid(row=6)

    mtLbl = Label(btnFrame, width=int(scrnWidth/70))
    mtLbl.grid(column=1, row=0)
    
                #Designing the button
    loginBtn = Button(btnFrame, text=login, command=clickLog,  fg="blue", bg="white", width=20, height=2)  
    loginBtn.grid(column=0, row=0, sticky="w")
    loginBtn.config(font=("Arial", 16))
    exBtn = Button(btnFrame, text=ex,   fg="blue", bg="white", width=10, height=2, command=exGui) 
    exBtn.grid(column = 2, row=0, sticky="e")
    exBtn.config(font=("Arial", 16))



                #Decide the size of the screen
    root.geometry(f'{scrnWidth}x{scrnHeight}+{-10}+{0}')
    root.attributes("-fullscreen", True)
    root.mainloop()



