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
import EEGReadData as erd 
import csv
import MobiClient as mc

fc3ar = np.array([])
fczar = np.array([])
fc4ar = np.array([])
c3ar = np.array([])
czar = np.array([])
c4ar = np.array([])
cp3ar = np.array([])
cpzar = np.array([])
cp4ar = np.array([])
# cond = False
end = False
running = False
painLevel = 0

def setSendTrue():
    global end
    end = True

def closeDataFile():
    global fileWriterData
    global fileWriterEvent
    global end
    end = False
    fileWriterData.close()
    fileWriterEvent.close()

def exitFromInstruction():
        root.destroy()

                    #Recieves a string and sets the username to it
def setUserName(userName):
    global user
    user = userName

def confirm():
#     global cond
#     cond = False
    # A boolean which controls the confirm button to open further Instruction windows.
    global running
    if running == False:
        global root
        running = True 
        global ins
        import Instructions as ins
        ins.instWriter(fileWriterEvent)
        threading.Thread(target=ins.initializeGui()).start()
        
    elif running == True:
        response = messagebox.showwarning(message=mesText)



#     ins.updateGui(root)
    # root.destroy()

                    # Popup message for confirming if the user really wants to exit
def exGui():
    # global cond
    updateDots(bgFc3)
    updateDots(bgFcz)
    updateDots(bgFc4)
    updateDots(bgCz)
    updateDots(bgCp3)
    # cond = True
    
    # ins.exGui()
    

def createCSVFiles():
    global temp
    temp = datetime.datetime.now()
    #channeldatas
    global fileNameData
    fileNameData = (str(temp.year) + str(temp.month) + str(temp.day)  
        + '-' + str(temp.hour) + ';'+ str(temp.minute) + '-data')
    createFileData = open("Reports\{}.csv".format(fileNameData), "w")
    createFileData.close()
    global fileWriterData
    fileWriterData = open("Reports\{}.csv".format(fileNameData), "w", newline='')
    fileWriterData.writelines("Time\t\tFC3,FCZ,FC4,C3 ,Cz ,C4 ,CP3,CPz,CP4\n")
    
    fileNameEvent = (str(temp.year) + str(temp.month) + str(temp.day)  
        + '-' + str(temp.hour)+ ';'+ str(temp.minute) + '-events')
    createFileEvent = open("Reports\{}.csv".format(fileNameEvent), "w")
    createFileEvent.close()
    global fileWriterEvent 
    fileWriterEvent = open("Reports\{}.csv".format(fileNameEvent), "w", newline='')
    fileWriterEvent.writelines("Patient:\t" + user + "\n")
    fileWriterEvent.writelines("Date and Time:\t" + str(datetime.datetime.now()) + "\n")
    fileWriterEvent.writelines("Pain level:\t" + str(painLevel) + "\n\n")

def writeToFile(fc3, fcz, fc4, c3, cz, c4, cp3, cpz, cp4):
    temp = datetime.datetime.now()
    time = str(temp.hour) +':'+ str(temp.minute)+':' + str(temp.second)+':'+str(temp.microsecond)
    
    sgnlWriter = csv.writer(fileWriterData, delimiter=',', quotechar='"', 
    quoting=csv.QUOTE_MINIMAL)
    sgnlWriter.writerow([time, str(fc3), str(fcz),
    str(fc4), str(c3), str(cz), str(c4), str(cp3),
    str(cpz), str(cp4)])

                                # New plot_data which brings signal for each channel
def plot_data():
    global end, fc3ar, fczar, fc4ar, c3ar, czar, c4ar, cp3ar, cpzar, cp4ar
    data = [0 for i in range(9)]
    for i in range(9):    
        connection = erd.checkSignal(i)
        data[i] = erd.getData(i, connection)

#     writeToFile(fc3, fcz, fc4, c3, cz, c4, cp3, cpz, cp4)
    if(end == True):
        writeToFile(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8])
        mc.sendDataToServer(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8])

# FC3
    if(len(fc3ar)<100):
        fc3ar = np.append(fc3ar, data[0])
        fczar = np.append(fczar, data[1])
        fc4ar = np.append(fc4ar, data[2])
        c3ar = np.append(c3ar, data[3])
        czar = np.append(czar, data[4])
        c4ar = np.append(c4ar, data[5])
        cp3ar = np.append(cp3ar, data[6])
        cpzar = np.append(cpzar, data[7])
        cp4ar = np.append(cp4ar, data[8])
    else:
        fc3ar[0:99] = fc3ar[1:100]
        fc3ar[99] = data[0]  
#Fcz
        fczar[0:99] = fczar[1:100]
        fczar[99] = data[1]  
#FC4
        fc4ar[0:99] = fc4ar[1:100]
        fc4ar[99] = data[2]  
#C3
        c3ar[0:99] = c3ar[1:100]
        c3ar[99] = data[3]      
#Cz
        czar[0:99] = czar[1:100]
        czar[99] = data[4]  
#C4
        c4ar[0:99] = c4ar[1:100]
        c4ar[99] = data[5]  
#CP3
        cp3ar[0:99] = cp3ar[1:100]
        cp3ar[99] = data[6]  
#Cpz
        cpzar[0:99] = czar[1:100]
        cpzar[99] = data[7]  
#CP4
        cp4ar[0:99] = cp4ar[1:100]
        cp4ar[99] = data[8]  
#fc3
    linesFc3.set_xdata(np.arange(0, len(fc3ar)))
    linesFc3.set_ydata(fc3ar)
    if(data[0] == -5):
        linesFc3.set_color('red')
        bgFc3.config(bg='red')
    else:
        linesFc3.set_color('green')
        bgFc3.config(bg='green')
    linesFc3.set_linewidth(0.5)
    canvasFc3.draw()
#fcz
    linesFcz.set_xdata(np.arange(0, len(fczar)))
    linesFcz.set_ydata(fczar)
    if(data[1] == -5):
        linesFcz.set_color('red')
        bgFcz.config(bg='red')
    else:
        linesFcz.set_color('green')
        bgFcz.config(bg='green')
    linesFcz.set_linewidth(0.5)
    canvasFcz.draw()
#fc4
    linesFc4.set_xdata(np.arange(0, len(fczar)))
    linesFc4.set_ydata(fc4ar)
    if(data[2] == -5):
        linesFc4.set_color('red')
        bgFc4.config(bg='red')
    else:
        linesFc4.set_color('green')
        bgFc4.config(bg='green')
    linesFc4.set_linewidth(0.5)
    canvasFc4.draw()
#c3
    linesC3.set_xdata(np.arange(0, len(c3ar)))
    linesC3.set_ydata(c3ar)
    if(data[3] == -5):
        linesC3.set_color('red')
        bgC3.config(bg='red')
    else:
        bgC3.config(bg='green')
        linesC3.set_color('green')
    linesC3.set_linewidth(0.5)
    canvasC3.draw()
#cz
    linesCz.set_xdata(np.arange(0, len(czar)))
    linesCz.set_ydata(czar)
    if(data[4] == -5):
        linesCz.set_color('red')
        bgCz.config(bg='red')
    else:
        linesCz.set_color('green')
        bgCz.config(bg='green')
    linesCz.set_linewidth(0.5)
    canvasCz.draw()
#c4
    linesC4.set_xdata(np.arange(0, len(c4ar)))
    linesC4.set_ydata(c4ar)
    if(data[5] == -5):
        linesC4.set_color('red')
        bgC4.config(bg='red')
    else:
        linesC4.set_color('green')
        bgC4.config(bg='green')
    linesC4.set_linewidth(0.5)
    canvasC4.draw()
#cp3
    linesCp3.set_xdata(np.arange(0, len(cp3ar)))
    linesCp3.set_ydata(cp3ar)
    if(data[6] == -5):
        linesCp3.set_color('red')
        bgCp3.config(bg='red')
    else:
        linesCp3.set_color('green')
        bgCp3.config(bg='green')
    linesCp3.set_linewidth(0.5)
    canvasCp3.draw()
#cpz
    linesCpz.set_xdata(np.arange(0, len(cpzar)))
    linesCpz.set_ydata(cpzar)
    if(data[7] == -5):
        linesCpz.set_color('red')
        bgCpz.config(bg='red')
    else:
        linesCpz.set_color('green')
        bgCpz.config(bg='green')
    linesCpz.set_linewidth(0.5)
    canvasCpz.draw()
#cp4
    linesCp4.set_xdata(np.arange(0, len(cp4ar)))
    linesCp4.set_ydata(cp4ar)
    if(data[8] == -5):
        linesCp4.set_color('red')
        bgCp4.config(bg='red')
    else:
        linesCp4.set_color('green')
        bgCp4.config(bg='green')
    linesCp4.set_linewidth(0.5)
    canvasCp4.draw()


    root.after(1, plot_data)

                     # Creates and shows the GUI
def initializeGui():
    global running
    running = False
    global exMessage
    readFile = open("TextSettings\ChosenLanguage.txt", "r")
    temp = readFile.readlines()
    temp1 = temp[0]
    chosenLang = open("TextSettings\{}.txt".format(temp1), "r", encoding='utf-8')
    language = chosenLang.readlines()

    barTitle = language[19].replace('\n', '')
    frTitle = language[20].replace('\n', '') + user
    conf = language[18].replace('\n', '')
    ex = language[6].replace('\n', '')
    exMessage = language[13].replace('\n', '')
    global mesText 
    mesText = language[31].replace('\n', '')

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

    createCSVFiles()

    root.after(1000, plot_data)
    root.mainloop()

def main():
    if __name__ == '__main__':
        initializeGui()

            #Updates the previous GUI with this GUI
def updateGui(rooti):
    global root
    root = rooti
    initializeGui()


def setVAS(vas):
    global painLevel
    painLevel = vas

def updateDots(lblDot):
    lblDot.config(bg='green')




