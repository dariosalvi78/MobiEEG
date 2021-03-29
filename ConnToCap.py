#This class connects the program to the Cap 
# and checks if it is proper placed 
#Author Rohan

from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import datetime
from tkinter import Canvas
import random
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np 
import serial as sr 
import time
import threading

fc3ar = np.array([])
fczar = np.array([])
fc4ar = np.array([])
c3ar = np.array([])
czar = np.array([])
c4ar = np.array([])
cp3ar = np.array([])
cpzar = np.array([])
cp4ar = np.array([])
cond = False
user = "Rohan"

def exitFromInstruction():
        root.destroy()
        
def rand():
    return random.randint(0,256)

                    #Recieves a string and sets the username to it
def setUserName(userName):
    global user
    user = userName

def confirm():
#     global cond
#     cond = False
    global root
    import Instructions as ins
    threading.Thread(target=ins.initializeGui()).start()
    
    

    
#     ins.updateGui(root)
    
    # root.destroy()

                    # Popup message for confirming if the user really wants to exit
def exGui():
    global cond
    updateDots(bgFc3)
    updateDots(bgFcz)
    updateDots(bgFc4)
    updateDots(bgCz)
    updateDots(bgCp3)
    cond = True
    # response = messagebox.askyesno(message=exMessage)
    # if response == 1:
    #     root.destroy()

#------------runs the signals
def plot_data():
    global cond, fc3ar, fczar, fc4ar, c3ar, czar, c4ar, cp3ar, cpzar, cp4ar
    fc3 = rand()
    fcz = rand()
    fc4 = rand()
    c3 = rand()
    cz = rand()
    c4 = rand()
    cp3 = rand()
    cpz = rand()
    cp4 = rand()

    if (cond == True):
        if(len (fc3ar)>100):
            fc3ar = np.append(fc3ar, fc3)
            fczar = np.append(fczar, fcz)
            fc4ar = np.append(fc4ar, fc4)
            c3ar = np.append(c3ar, c3)
            czar = np.append(czar, cz)
            c4ar = np.append(c4ar, c4)
            cp3ar = np.append(cp3ar, cp3)
            cpzar = np.append(cpzar, cpz)
            cp4ar = np.append(cp4ar, cp4)
        else:
            # FC3
            fc3ar[0:99] = fc3ar[1:100]
            fc3ar[99] = fc3  
            linesFc3.set_xdata(np.arange(0, len(fc3ar)))
            linesFc3.set_ydata(fc3ar)
            linesFc3.set_color('green')
            linesFc3.set_linewidth(0.5)
            canvasFc3.draw()
        #     print(fc3ar[99])
            #Fcz
            fczar[0:99] = fczar[1:100]
            fczar[99] = fcz  
            linesFcz.set_xdata(np.arange(0, len(fczar)))
            linesFcz.set_ydata(fczar)
            linesFcz.set_color('green')
            linesFcz.set_linewidth(0.5)
            canvasFcz.draw()
            #FC4
            fc4ar[0:99] = fc4ar[1:100]
            fc4ar[99] = fc4  
            linesFc4.set_xdata(np.arange(0, len(fc4ar)))
            linesFc4.set_ydata(fc4ar)
            linesFc4.set_color('green')
            linesFc4.set_linewidth(0.5)
            canvasFc4.draw()
            #C3
        #     c3ar[0:99] = c3ar[1:100]
        #     c3ar[99] = c3  
        #     linesC3.set_xdata(np.arange(0, len(c3ar)))
        #     linesC3.set_ydata(c3ar)
        #     linesC3.set_color('green')
        #     linesC3.set_linewidth(0.5)
        #     canvasC3.draw()
            #Cz
            czar[0:99] = czar[1:100]
            czar[99] = cz  
            linesCz.set_xdata(np.arange(0, len(czar)))
            linesCz.set_ydata(czar)
            linesCz.set_color('green')
            linesCz.set_linewidth(0.5)
            canvasCz.draw()
            #C4
        #     c4ar[0:99] = c4ar[1:100]
        #     c4ar[99] = c4  
        #     linesC4.set_xdata(np.arange(0, len(c4ar)))
        #     linesC4.set_ydata(c4ar)
        #     linesC4.set_color('green')
        #     linesC4.set_linewidth(0.5)
        #     canvasC4.draw()
            # #CP3
            cp3ar[0:99] = cp3ar[1:100]
            cp3ar[99] = cp3  
            linesCp3.set_xdata(np.arange(0, len(cp3ar)))
            linesCp3.set_ydata(cp3ar)
            linesCp3.set_color('green')
            linesCp3.set_linewidth(0.5)
            canvasCp3.draw()
            # #Cpz
        #     cpzar[0:99] = czar[1:100]
        #     cpzar[99] = cz  
        #     linesCpz.set_xdata(np.arange(0, len(cpzar)))
        #     linesCpz.set_ydata(cpzar)
        #     linesCpz.set_color('green')
        #     linesCpz.set_linewidth(0.5)
        #     canvasCpz.draw()
            # #CP4
        #     cp4ar[0:99] = cp4ar[1:100]
        #     cp4ar[99] = cp4  
        #     linesCp4.set_xdata(np.arange(0, len(cp4ar)))
        #     linesCp4.set_ydata(cp4ar)
        #     linesCp4.set_color('green')
        #     linesCp4.set_linewidth(0.5)
        #     canvasCp4.draw()
        # # root.after(20, plot_data)
    else:
        a = -5
        if(len (fc3ar)<100):
            fc3ar = np.append(fc3ar, a)
            fczar = np.append(fczar, a)
            fc4ar = np.append(fc4ar, a)
            c3ar = np.append(c3ar, a)
            czar = np.append(czar, a)
            c4ar = np.append(c4ar, a)
            cp3ar = np.append(cp3ar, a)
            cpzar = np.append(cpzar, a)
            cp4ar = np.append(cp4ar, a)
        else:
            #FC3
            fc3ar[0:99] = fc3ar[1:100]
            fc3ar[99] = a  
            linesFc3.set_xdata(np.arange(0, len(fc3ar)))
            linesFc3.set_ydata(fc3ar)
            linesFc3.set_color('red')
            linesFc3.set_linewidth(0.5)
            canvasFc3.draw()
            # FCz
            fczar[0:99] = fczar[1:100]
            fczar[99] = a  
            linesFcz.set_xdata(np.arange(0, len(fczar)))
            linesFcz.set_ydata(fczar)
            linesFcz.set_color('red')
            linesFcz.set_linewidth(0.5)
            canvasFcz.draw()
            #FC4
            fc4ar[0:99] = fc4ar[1:100]
            fc4ar[99] = a  
            linesFc4.set_xdata(np.arange(0, len(fc4ar)))
            linesFc4.set_ydata(fc4ar)
            linesFc4.set_color('red')
            linesFc4.set_linewidth(0.5)
            canvasFc4.draw()
            #C3
            c3ar[0:99] = c3ar[1:100]
            c3ar[99] = a  
            linesC3.set_xdata(np.arange(0, len(c3ar)))
            linesC3.set_ydata(c3ar)
            linesC3.set_color('red')
            linesC3.set_linewidth(0.5)
            canvasC3.draw()
            #Cz
            czar[0:99] = czar[1:100]
            czar[99] = a  
            linesCz.set_xdata(np.arange(0, len(czar)))
            linesCz.set_ydata(czar)
            linesCz.set_color('red')
            linesCz.set_linewidth(0.5)
            canvasCz.draw()
            #C4
            c4ar[0:99] = c4ar[1:100]
            c4ar[99] = a  
            linesC4.set_xdata(np.arange(0, len(c4ar)))
            linesC4.set_ydata(c4ar)
            linesC4.set_color('red')
            linesC4.set_linewidth(0.5)
            canvasC4.draw()
            # #CP3
            cp3ar[0:99] = cp3ar[1:100]
            cp3ar[99] = a  
            linesCp3.set_xdata(np.arange(0, len(cp3ar)))
            linesCp3.set_ydata(cp3ar)
            linesCp3.set_color('red')
            linesCp3.set_linewidth(0.5)
            canvasCp3.draw()
            # #CPz
            cpzar[0:99] = cpzar[1:100]
            cpzar[99] = a  
            linesCpz.set_xdata(np.arange(0, len(cpzar)))
            linesCpz.set_ydata(cpzar)
            linesCpz.set_color('red')
            linesCpz.set_linewidth(0.5)
            canvasCpz.draw()
            #CP4
            cp4ar[0:99] = cp4ar[1:100]
            cp4ar[99] = a  
            linesCp4.set_xdata(np.arange(0, len(cp4ar)))
            linesCp4.set_ydata(cp4ar)
            linesCp4.set_color('red')
            linesCp4.set_linewidth(0.5)
            canvasCp4.draw()
    root.after(1, plot_data)

                     # Creates and shows the GUI
def initializeGui():

    global exMessage
    readFile = open("LanguageSettings\ChosenLanguage.txt", "r")
    temp = readFile.readlines()
    temp1 = temp[0]
    chosenLang = open("LanguageSettings\{}.txt".format(temp1), "r", encoding='utf-8')
    language = chosenLang.readlines()

    barTitle = language[19].replace('\n', '')
    frTitle = language[20].replace('\n', '') + user
    conf = language[18].replace('\n', '')
    ex = language[6].replace('\n', '')
    exMessage = language[13].replace('\n', '')

    root.title(barTitle + user)
    scrnWidth = root.winfo_screenwidth()
    scrnHeight = root.winfo_screenheight()
    
    GuiFrame = LabelFrame(root, text=frTitle, pady=scrnHeight/400)
    GuiFrame.grid(column=0, row=0)#, padx=scrnWidth/30, pady= scrnHeight/30, ipadx=scrnWidth/20, ipady=0)
    GuiFrame.config(font=("Arial", 20))
    
    imgFrame = LabelFrame(GuiFrame, borderwidth=0)#, padx=scrnWidth/800, pady=scrnHeight/800)
    imgFrame.grid(column=0, row=0, padx=scrnWidth/80)#, padx=scrnWidth/40, pady= scrnHeight/70)
    chartFrame = LabelFrame(GuiFrame, borderwidth=0)
    chartFrame.grid(column=1, row=0)
    global animFrame
    animFrame = LabelFrame(chartFrame, borderwidth=0)
    animFrame.grid(column=0, row=0 )
    btnFrame = LabelFrame(chartFrame, borderwidt=0)
    btnFrame.grid(column=0, row=1)

    image = Image.open("Images\CapMap1.png")
    bgImage = ImageTk.PhotoImage(image)
    background = Label(imgFrame, image =bgImage, borderwidth=0)
    background.grid(column=0,row=0)
    
            #Dots
    lblDots = Label(imgFrame)
    lblDots.place(x = scrnWidth/11, y=scrnHeight/3.1)
            #FC3
    global bgFc3
    bgFc3 = Label(lblDots, text= 'FC3', bg='red', width=5, height=1)
    bgFc3.grid(column=0,row=0)
            #FCz
    global bgFcz
    bgFcz = Label(lblDots, text= 'FCz', bg='red', width=5, height=1)
    bgFcz.grid(column=1,row=0)
            #FC4
    global bgFc4
    bgFc4 = Label(lblDots, text= 'FC4', bg='red', width=5, height=1)
    bgFc4.grid(column=2,row=0)
            #C3
    global bgC3
    bgC3 = Label(lblDots, text= 'C3', bg='red', width=5, height=1)
    bgC3.grid(column=0,row=1,)
            #Cz
    global bgCz
    bgCz = Label(lblDots, text= 'Cz', bg='red', width=5, height=1)
    bgCz.grid(column=1,row=1, padx=20, pady=20)
            #C4
    global bgC4
    bgC4 = Label(lblDots, text= 'C4', bg='red', width=5, height=1)
    bgC4.grid(column=2,row=1)
            #CP3
    global bgCp3
    bgCp3 = Label(lblDots, text= 'CP3', bg='red', width=5, height=1)
    bgCp3.grid(column=0,row=2)
            #CPz
    global bgCpz
    bgCpz = Label(lblDots, text= 'CPz', bg='red', width=5, height=1)
    bgCpz.grid(column=1,row=2)
            #CP4
    global bgCp4
    bgCp4 = Label(lblDots, text= 'CP4', bg='red', width=5, height=1)
    bgCp4.grid(column=2,row=2)

    lblDotFrame = LabelFrame(animFrame, width=10, height=800, borderwidth=0)
    lblDotFrame.grid(column=0, row=0)
    chartLbls = ['FC3', 'FCz', 'FC4', 'C3', 'Cz', 'C4', 'CP3', 'CPz', 'CP4']
    for i, j in enumerate(chartLbls):
        lbl = 'lbl' + str(i)
        lbl = Label(lblDotFrame, height=3, width=3, text=j, 
        bg='white', anchor='w', borderwidth=1)
        lbl.grid(column=0, row=i)

    #initializeChart()
    lblCanvas = LabelFrame(animFrame, width=700, height=440, bg='light blue',
    borderwidth=0)
    lblCanvas.grid(column=1, row=0)
            #FC3
    figFc3 = Figure()
    axFc3 = figFc3.add_subplot(111)
    axFc3.set_title('FC3')
    axFc3.set_xlabel('')
    axFc3.set_ylabel('')
    axFc3.set_xlim(0, 100)
    axFc3.set_ylim(-10,400)
    global linesFc3
    linesFc3 = axFc3.plot([],[])[0]
    global canvasFc3
    canvasFc3 = FigureCanvasTkAgg(figFc3, master=lblCanvas)
    canvasFc3.get_tk_widget().place(x=0, y=0, width=750, height=50)
    canvasFc3.draw()  

    # root.update()
            #FCz
    figFcz = Figure()
    axFcz = figFcz.add_subplot(111)
    axFcz.set_title('FC3')
    axFcz.set_xlabel('')
    axFcz.set_ylabel('')
    axFcz.set_xlim(0, 100)
    axFcz.set_ylim(-10,400)
    global linesFcz
    linesFcz = axFcz.plot([],[])[0]
    global canvasFcz
    canvasFcz = FigureCanvasTkAgg(figFcz, master=lblCanvas)
    canvasFcz.get_tk_widget().place(x=0, y=50, width=750, height=50)
    canvasFcz.draw()
            #FC4
    figFc4 = Figure()
    axFc4 = figFc4.add_subplot(111)
    axFc4.set_title('FC3')
    axFc4.set_xlabel('')
    axFc4.set_ylabel('')
    axFc4.set_xlim(0, 100)
    axFc4.set_ylim(-10,400)
    global linesFc4
    linesFc4 = axFc4.plot([],[])[0]
    global canvasFc4
    canvasFc4 = FigureCanvasTkAgg(figFc4, master=lblCanvas)
    canvasFc4.get_tk_widget().place(x=0, y=100, width=750, height=50)
    canvasFc4.draw()
            #C3
    figC3 = Figure()
    axC3 = figC3.add_subplot(111)
    axC3.set_title('FC3')
    axC3.set_xlabel('')
    axC3.set_ylabel('')
    axC3.set_xlim(0, 100)
    axC3.set_ylim(-10,400)
    global linesC3
    linesC3 = axC3.plot([],[])[0]
    global canvasC3
    canvasC3 = FigureCanvasTkAgg(figC3, master=lblCanvas)
    canvasC3.get_tk_widget().place(x=0, y=150, width=750, height=50)
    canvasC3.draw()
            #Cz
    figCz = Figure()
    axCz = figCz.add_subplot(111)
    axCz.set_title('FC3')
    axCz.set_xlabel('')
    axCz.set_ylabel('')
    axCz.set_xlim(0, 100)
    axCz.set_ylim(-10,400)
    global linesCz
    linesCz = axCz.plot([],[])[0]
    global canvasCz
    canvasCz = FigureCanvasTkAgg(figCz, master=lblCanvas)
    canvasCz.get_tk_widget().place(x=0, y=200, width=750, height=50)
    canvasCz.draw()
            #C4
    figC4 = Figure()
    axC4 = figC4.add_subplot(111)
    axC4.set_title('FC3')
    axC4.set_xlabel('')
    axC4.set_ylabel('')
    axC4.set_xlim(0, 100)
    axC4.set_ylim(-10,400)
    global linesC4
    linesC4 = axC4.plot([],[])[0]
    global canvasC4
    canvasC4 = FigureCanvasTkAgg(figC4, master=lblCanvas)
    canvasC4.get_tk_widget().place(x=0, y=250, width=750, height=50)
    canvasC4.draw()
            #CP3
    figCp3 = Figure()
    axCp3 = figCp3.add_subplot(111)
    axCp3.set_title('FC3')
    axCp3.set_xlabel('')
    axCp3.set_ylabel('')
    axCp3.set_xlim(0, 100)
    axCp3.set_ylim(-10,400)
    global linesCp3
    linesCp3 = axCp3.plot([],[])[0]
    global canvasCp3
    canvasCp3 = FigureCanvasTkAgg(figCp3, master=lblCanvas)
    canvasCp3.get_tk_widget().place(x=0, y=300, width=750, height=50)
    canvasCp3.draw()
            #CPz
    figCpz = Figure()
    axCpz = figCpz.add_subplot(111)
    axCpz.set_title('FC3')
    axCpz.set_xlabel('')
    axCpz.set_ylabel('')
    axCpz.set_xlim(0, 100)
    axCpz.set_ylim(-10,400)
    global linesCpz
    linesCpz = axCpz.plot([],[])[0]
    global canvasCpz
    canvasCpz = FigureCanvasTkAgg(figCpz, master=lblCanvas)
    canvasCpz.get_tk_widget().place(x=0, y=350, width=750, height=50)
    canvasCpz.draw()
            #CP4
    figCp4 = Figure()
    axCp4 = figCp4.add_subplot(111)
    axCp4.set_title('FC3')
    axCp4.set_xlabel('')
    axCp4.set_ylabel('')
    axCp4.set_xlim(0, 100)
    axCp4.set_ylim(-10,400)
    global linesCp4
    linesCp4 = axCp4.plot([],[])[0]
    global canvasCp4
    canvasCp4 = FigureCanvasTkAgg(figCp4, master=lblCanvas)
    canvasCp4.get_tk_widget().place(x=0, y=400, width=750, height=40)
    canvasCp4.draw()

            #Button
    btnCon = Button(btnFrame, text=conf, command=confirm,
        fg="blue", width=int(scrnWidth/100), height=int(scrnHeight/400))
    btnCon.grid(column=0, row=0, sticky="s")
    btnCon.config(font=("Arial", 18))
    lblBtn = LabelFrame(btnFrame, width=scrnWidth/8, borderwidth=0)
    lblBtn.grid(column=1, row=0, sticky='e')
    btnEx = Button(btnFrame, text=ex, command=exGui, fg="blue", width=int(scrnWidth/100), height=int(scrnHeight/400))
    btnEx.grid(column=2, row=0, sticky='s')
    btnEx.config(font=("Arial", 18))

    #Decides the size of the screen
    root.geometry(f'{scrnWidth}x{scrnHeight}+{-10}+{0}')
    root.attributes("-fullscreen", True)
    root.after(1, plot_data)
    root.mainloop()
#     root.after(1, plot_data)

def main():
    if __name__ == '__main__':
        initializeGui()

            #Updates the previous GUI with this GUI
def updateGui(rooti):
    global root
    root = rooti
    initializeGui()

def updateDots( lblDot):
    lblDot.config(bg='green')


