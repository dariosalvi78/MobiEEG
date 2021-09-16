'''
Shows the signals and datas. The graph ui updates 3 times per second. 
@uthor Rohan Samandari
'''
import Settings
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import Canvas
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import EEGReadData as erd
import csv
import EEGToCSV as ecs

fc3ar = np.array([])
fczar = np.array([])
fc4ar = np.array([])
c3ar = np.array([])
czar = np.array([])
c4ar = np.array([])
cp3ar = np.array([])
cpzar = np.array([])
cp4ar = np.array([])

threadStop = False
end = False
running = False
painLevel = 0
chImp0 = chImp1 = chImp2 = chImp3 = chImp4 = chImp5 = chImp6 = chImp7 = chImp8 = "ImpedanceLevel.UNKNOWN"
copy0 = 0
sigCounter = 0
fileWriterEvent = 0


def closeDataFile():
    # Closes the files
    global fileWriterEvent
    global end
    end = False
    fileWriterData = ecs.getFileWriterData()
    fileWriterData.close()
    fileWriterEvent.close()


def setUserName(userName):
    # Recieves a string and sets the username to it
    global user
    user = userName


def confirm():
    # Instruction Gui is called and this ui destroys
    global ins, threadStop
    import Instructions as ins
    fileWriterEvent = ecs.getFileWriterEvent()
    ins.instWriter(fileWriterEvent)
    threadStop = True
    root.destroy()
    ins.initializeGui()


def exGui():
    # Popup message for confirming if the user really wants to exit
    global threadStop, running, root, ins
    response = messagebox.askyesno(message=exMessage)
    if response == 1:
        threadStop = True
        erd.setMainConnection()
        if(running == False):
            root.destroy()
        else:
            ins.exGui()


sc = 0


def plot_data():
    # Running, showing and updating the graph ui
    global sc, threadStop, end, sigCounter
    global axFc3, axFcz, axFc4, axC3, axCz, axZ4, axCp3, axCpz, axCp4
    global fc3ar, fczar, fc4ar, c3ar, czar, c4ar, cp3ar, cpzar, cp4ar
    global chImp0, chImp1, chImp2, chImp3, chImp4, chImp5, chImp6, chImp7, chImp8
    chann0, chann1, chann2, chann3, chann4, chann5, chann6, chann7, chann8 = erd.getData()
    chImp0, chImp1, chImp2, chImp3, chImp4, chImp5, chImp6, chImp7, chImp8 = erd.getImpedanceLevel()

# FC3
    if(len(fc3ar) < 100):
        fc3ar = np.append(fc3ar, chann0)
        fczar = np.append(fczar, chann1)
        fc4ar = np.append(fc4ar, chann2)
        c3ar = np.append(c3ar, chann3)
        czar = np.append(czar, chann4)
        c4ar = np.append(c4ar, chann5)
        cp3ar = np.append(cp3ar, chann6)
        cpzar = np.append(cpzar, chann7)
        cp4ar = np.append(cp4ar, chann8)
    else:
        fc3ar[0:99] = fc3ar[1:100]
        fc3ar[99] = chann0
# Fcz
        fczar[0:99] = fczar[1:100]
        fczar[99] = chann1
# FC4
        fc4ar[0:99] = fc4ar[1:100]
        fc4ar[99] = chann2
# C3
        c3ar[0:99] = c3ar[1:100]
        c3ar[99] = chann3
# Cz
        czar[0:99] = czar[1:100]
        czar[99] = chann4
# C4
        c4ar[0:99] = c4ar[1:100]
        c4ar[99] = chann5
# CP3
        cp3ar[0:99] = cp3ar[1:100]
        cp3ar[99] = chann6
# Cpz
        cpzar[0:99] = cpzar[1:100]
        cpzar[99] = chann7
# CP4
        cp4ar[0:99] = cp4ar[1:100]
        cp4ar[99] = chann8
# fc3
    linesFc3.set_xdata(np.arange(0, len(fc3ar)))
    linesFc3.set_ydata(fc3ar)
    if(sigCounter == 0):
        axFc3.set_ylim(chann0-2000, chann0 + 2000)

    if(chImp0 == "ImpedanceLevel.UNKNWON"):
        linesFc3.set_color('red')
        bgFc3.config(bg='gray')
    if(chImp0 == "ImpedanceLevel.SATURATED"):
        linesFc3.set_color('red')
        bgFc3.config(bg='red')
    elif(chImp0 == "ImpedanceLevel.BAD"):
        linesFc3.set_color('green')
        bgFc3.config(bg='orange')
    elif(chImp0 == "ImpedanceLevel.FAIR"):
        linesFc3.set_color('green')
        bgFc3.config(bg='yellow')
    elif(chImp0 == "ImpedanceLevel.GOOD"):
        linesFc3.set_color('green')
        bgFc3.config(bg='green')
    linesFc3.set_linewidth(0.5)
    canvasFc3.draw()
# fcz
    linesFcz.set_xdata(np.arange(0, len(fczar)))
    linesFcz.set_ydata(fczar)
    if(sigCounter == 0):
        axFcz.set_ylim(chann1-2000, chann1 + 2000)

    if(chImp1 == "ImpedanceLevel.UNKNWON"):
        linesFcz.set_color('red')
        bgFcz.config(bg='gray')
    if(chImp1 == "ImpedanceLevel.SATURATED"):
        linesFcz.set_color('red')
        bgFcz.config(bg='red')
    elif(chImp1 == "ImpedanceLevel.BAD"):
        linesFcz.set_color('green')
        bgFcz.config(bg='orange')
    elif(chImp1 == "ImpedanceLevel.FAIR"):
        linesFcz.set_color('green')
        bgFcz.config(bg='yellow')
    elif(chImp1 == "ImpedanceLevel.GOOD"):
        linesFcz.set_color('green')
        bgFcz.config(bg='green')
    linesFcz.set_linewidth(0.5)
    canvasFcz.draw()
# fc4
    linesFc4.set_xdata(np.arange(0, len(fczar)))
    linesFc4.set_ydata(fc4ar)
    if(sigCounter == 0):
        axFc4.set_ylim(chann2-2000, chann2 + 2000)
    if(chImp2 == "ImpedanceLevel.UNKNWON"):
        linesFc4.set_color('red')
        bgFc4.config(bg='gray')
    if(chImp2 == "ImpedanceLevel.SATURATED"):
        linesFc4.set_color('red')
        bgFc4.config(bg='red')
    elif(chImp2 == "ImpedanceLevel.BAD"):
        linesFc4.set_color('green')
        bgFc4.config(bg='orange')
    elif(chImp2 == "ImpedanceLevel.FAIR"):
        linesFc4.set_color('green')
        bgFc4.config(bg='yellow')
    elif(chImp2 == "ImpedanceLevel.GOOD"):
        linesFc4.set_color('green')
        bgFc4.config(bg='green')
    linesFc4.set_linewidth(0.5)
    canvasFc4.draw()
# c3
    linesC3.set_xdata(np.arange(0, len(c3ar)))
    linesC3.set_ydata(c3ar)
    if(sigCounter == 0):
        axC3.set_ylim(chann3-2000, chann3 + 2000)
    if(chImp3 == "ImpedanceLevel.UNKNWON"):
        linesC3.set_color('red')
        bgC3.config(bg='gray')
    if(chImp3 == "ImpedanceLevel.SATURATED"):
        linesC3.set_color('red')
        bgC3.config(bg='red')
    elif(chImp3 == "ImpedanceLevel.BAD"):
        linesC3.set_color('green')
        bgC3.config(bg='orange')
    elif(chImp3 == "ImpedanceLevel.FAIR"):
        linesC3.set_color('green')
        bgC3.config(bg='yellow')
    elif(chImp3 == "ImpedanceLevel.GOOD"):
        linesC3.set_color('green')
        bgC3.config(bg='green')
    linesC3.set_linewidth(0.5)
    canvasC3.draw()
# cz
    linesCz.set_xdata(np.arange(0, len(czar)))
    linesCz.set_ydata(czar)
    if(sigCounter == 0):
        axCz.set_ylim(chann4-2000, chann4 + 2000)
    if(chImp4 == "ImpedanceLevel.UNKNWON"):
        linesCz.set_color('red')
        bgCz.config(bg='gray')
    if(chImp4 == "ImpedanceLevel.SATURATED"):
        linesCz.set_color('red')
        bgCz.config(bg='red')
    elif(chImp4 == "ImpedanceLevel.BAD"):
        linesCz.set_color('green')
        bgCz.config(bg='orange')
    elif(chImp4 == "ImpedanceLevel.FAIR"):
        linesCz.set_color('green')
        bgCz.config(bg='yellow')
    elif(chImp4 == "ImpedanceLevel.GOOD"):
        linesCz.set_color('green')
        bgCz.config(bg='green')
    linesCz.set_linewidth(0.5)
    canvasCz.draw()
# c4
    linesC4.set_xdata(np.arange(0, len(c4ar)))
    linesC4.set_ydata(c4ar)
    if(sigCounter == 0):
        axC4.set_ylim(chann5-2000, chann5 + 2000)
    if(chImp5 == "ImpedanceLevel.UNKNWON"):
        linesC4.set_color('red')
        bgC4.config(bg='gray')
    if(chImp5 == "ImpedanceLevel.SATURATED"):
        linesC4.set_color('red')
        bgC4.config(bg='red')
    elif(chImp5 == "ImpedanceLevel.BAD"):
        linesC4.set_color('green')
        bgC4.config(bg='orange')
    elif(chImp5 == "ImpedanceLevel.FAIR"):
        linesC4.set_color('green')
        bgC4.config(bg='yellow')
    elif(chImp5 == "ImpedanceLevel.GOOD"):
        linesC4.set_color('green')
        bgC4.config(bg='green')
    linesC4.set_linewidth(0.5)
    canvasC4.draw()
# cp3
    linesCp3.set_xdata(np.arange(0, len(cp3ar)))
    linesCp3.set_ydata(cp3ar)
    if(sigCounter == 0):
        axCp3.set_ylim(chann6-2000, chann6 + 2000)
    if(chImp6 == "ImpedanceLevel.UNKNWON"):
        linesCp3.set_color('red')
        bgCp3.config(bg='gray')
    if(chImp6 == "ImpedanceLevel.SATURATED"):
        linesCp3.set_color('red')
        bgCp3.config(bg='red')
    elif(chImp6 == "ImpedanceLevel.BAD"):
        linesCp3.set_color('green')
        bgCp3.config(bg='orange')
    elif(chImp6 == "ImpedanceLevel.FAIR"):
        linesCp3.set_color('green')
        bgCp3.config(bg='yellow')
    elif(chImp6 == "ImpedanceLevel.GOOD"):
        linesCp3.set_color('green')
        bgCp3.config(bg='green')
    linesCp3.set_linewidth(0.5)
    canvasCp3.draw()
# cpz
    linesCpz.set_xdata(np.arange(0, len(cpzar)))
    linesCpz.set_ydata(cpzar)
    if(sigCounter == 0):
        axCpz.set_ylim(chann7-2000, chann7 + 2000)
    if(chImp7 == "ImpedanceLevel.UNKNWON"):
        linesCpz.set_color('red')
        bgCpz.config(bg='gray')
    if(chImp7 == "ImpedanceLevel.SATURATED"):
        linesCpz.set_color('red')
        bgCpz.config(bg='red')
    elif(chImp7 == "ImpedanceLevel.BAD"):
        linesCpz.set_color('green')
        bgCpz.config(bg='orange')
    elif(chImp7 == "ImpedanceLevel.FAIR"):
        linesCpz.set_color('green')
        bgCpz.config(bg='yellow')
    elif(chImp7 == "ImpedanceLevel.GOOD"):
        linesCpz.set_color('green')
        bgCpz.config(bg='green')
    linesCpz.set_linewidth(0.5)
    canvasCpz.draw()
# cp4
    linesCp4.set_xdata(np.arange(0, len(cp4ar)))
    linesCp4.set_ydata(cp4ar)
    if(sigCounter == 0):
        axCp4.set_ylim(chann8-2000, chann8 + 2000)
        sigCounter = -10

    if(chImp8 == "ImpedanceLevel.UNKNWON"):
        linesCp4.set_color('red')
        bgCp4.config(bg='gray')
    if(chImp8 == "ImpedanceLevel.SATURATED"):
        linesCp4.set_color('red')
        bgCp4.config(bg='red')
    elif(chImp8 == "ImpedanceLevel.BAD"):
        linesCp4.set_color('green')
        bgCp4.config(bg='orange')
    elif(chImp8 == "ImpedanceLevel.FAIR"):
        linesCp4.set_color('green')
        bgCp4.config(bg='yellow')
    elif(chImp8 == "ImpedanceLevel.GOOD"):
        linesCp4.set_color('green')
        bgCp4.config(bg='green')
    linesCp4.set_linewidth(0.5)
    canvasCp4.draw()

    if(threadStop == False):
        sigCounter += 1
        root.after(1, plot_data)


def initializeGui():
    # Creates and shows the GUI

    global running, exMessage
    running = False
    chosenLang = open(
        "i18n/{}.txt".format(Settings.settings['language']), "r", encoding='utf-8')
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
    GuiFrame.grid(column=0, row=0)
    GuiFrame.config(font=("Arial", 20))

    imgFrame = LabelFrame(GuiFrame, borderwidth=0)
    imgFrame.grid(column=0, row=0, padx=scrnWidth/80)
    chartFrame = LabelFrame(GuiFrame, borderwidth=0)
    chartFrame.grid(column=1, row=0)
    global animFrame
    animFrame = LabelFrame(chartFrame, borderwidth=0)
    animFrame.grid(column=0, row=0)
    btnFrame = LabelFrame(chartFrame, borderwidt=0)
    btnFrame.grid(column=0, row=1)

    image = Image.open("Images/CapMap1.png")
    bgImage = ImageTk.PhotoImage(image)
    background = Label(imgFrame, image=bgImage, borderwidth=0)
    background.grid(column=0, row=0)

    # Dots
    lblDots = Label(imgFrame)
    lblDots.place(x=scrnWidth/11, y=scrnHeight/3.1)
    # FC3
    global bgFc3
    bgFc3 = Label(lblDots, text='FC3', bg='gray', width=5, height=1)
    bgFc3.grid(column=0, row=0)
    # FCz
    global bgFcz
    bgFcz = Label(lblDots, text='FCz', bg='gray', width=5, height=1)
    bgFcz.grid(column=1, row=0)
    # FC4
    global bgFc4
    bgFc4 = Label(lblDots, text='FC4', bg='gray', width=5, height=1)
    bgFc4.grid(column=2, row=0)
    # C3
    global bgC3
    bgC3 = Label(lblDots, text='C3', bg='gray', width=5, height=1)
    bgC3.grid(column=0, row=1,)
    # Cz
    global bgCz
    bgCz = Label(lblDots, text='Cz', bg='gray', width=5, height=1)
    bgCz.grid(column=1, row=1, padx=20, pady=20)
    # C4
    global bgC4
    bgC4 = Label(lblDots, text='C4', bg='gray', width=5, height=1)
    bgC4.grid(column=2, row=1)
    # CP3
    global bgCp3
    bgCp3 = Label(lblDots, text='CP3', bg='gray', width=5, height=1)
    bgCp3.grid(column=0, row=2)
    # CPz
    global bgCpz
    bgCpz = Label(lblDots, text='CPz', bg='gray', width=5, height=1)
    bgCpz.grid(column=1, row=2)
    # CP4
    global bgCp4
    bgCp4 = Label(lblDots, text='CP4', bg='gray', width=5, height=1)
    bgCp4.grid(column=2, row=2)

    lblDotFrame = LabelFrame(animFrame, width=10, height=800, borderwidth=0)
    lblDotFrame.grid(column=0, row=0)
    chartLbls = ['FC3', 'FCz', 'FC4', 'C3', 'Cz', 'C4', 'CP3', 'CPz', 'CP4']
    for i, j in enumerate(chartLbls):
        lbl = 'lbl' + str(i)
        lbl = Label(lblDotFrame, height=3, width=3, text=j,
                    bg='white', anchor='w', borderwidth=1)
        lbl.grid(column=0, row=i)

    lblCanvas = LabelFrame(animFrame, width=700, height=440, bg='light blue',
                           borderwidth=0)
    lblCanvas.grid(column=1, row=0)

    global axFc3, axFcz, axFc4, axC3, axCz, axC4, axCp3, axCpz, axCp4
    # FC3 0
    figFc3 = Figure()
    axFc3 = figFc3.add_subplot(111)
    axFc3.set_title('FC3')
    axFc3.tick_params(labelcolor='w', left=False)
    # axFc3.set_xlabel('')
    # axFc3.set_ylabel('')
    axFc3.set_xlim(0, 100)
    axFc3.set_xticks([])
    axFc3.set_ylim(-100000, 100000)
    global linesFc3
    linesFc3 = axFc3.plot([], [])[0]
    global canvasFc3
    canvasFc3 = FigureCanvasTkAgg(figFc3, master=lblCanvas)
    canvasFc3.get_tk_widget().place(x=0, y=0, width=750, height=50)
    # canvasFc3.get_tk_widget().place(x=0, y=0, width=750, height=50)
    canvasFc3.draw()

    # FCz 1
    figFcz = Figure()
    axFcz = figFcz.add_subplot(111)
    axFcz.set_title('FC3')
    axFcz.set_xlim(0, 100)
    axFcz.set_ylim(-100000, 100000)
    axFcz.tick_params(labelcolor='w', left=False)

    global linesFcz
    linesFcz = axFcz.plot([], [])[0]
    global canvasFcz
    canvasFcz = FigureCanvasTkAgg(figFcz, master=lblCanvas)
    canvasFcz.get_tk_widget().place(x=0, y=50, width=750, height=50)
    canvasFcz.draw()
    # FC4 2
    figFc4 = Figure()
    axFc4 = figFc4.add_subplot(111)
    axFc4.set_title('FC3')
    axFc4.set_xlim(0, 100)
    axFc4.set_ylim(-100000, 100000)
    axFc4.tick_params(labelcolor='w', left=False)

    global linesFc4
    linesFc4 = axFc4.plot([], [])[0]
    global canvasFc4
    canvasFc4 = FigureCanvasTkAgg(figFc4, master=lblCanvas)
    canvasFc4.get_tk_widget().place(x=0, y=100, width=750, height=50)
    canvasFc4.draw()
    # C3 3
    figC3 = Figure()
    axC3 = figC3.add_subplot(111)
    axC3.set_title('FC3')
    axC3.set_xlim(0, 100)
    axC3.set_ylim(-100000, 100000)
    axC3.tick_params(labelcolor='w', left=False)

    global linesC3
    linesC3 = axC3.plot([], [])[0]
    global canvasC3
    canvasC3 = FigureCanvasTkAgg(figC3, master=lblCanvas)
    canvasC3.get_tk_widget().place(x=0, y=150, width=750, height=50)
    canvasC3.draw()
    # Cz 4
    figCz = Figure()
    axCz = figCz.add_subplot(111)
    axCz.set_title('FC3')
    axCz.set_xlim(0, 100)
    axCz.set_ylim(-100000, 100000)
    axCz.tick_params(labelcolor='w', left=False)

    global linesCz
    linesCz = axCz.plot([], [])[0]
    global canvasCz
    canvasCz = FigureCanvasTkAgg(figCz, master=lblCanvas)
    canvasCz.get_tk_widget().place(x=0, y=200, width=750, height=50)
    canvasCz.draw()
    # C4 5
    figC4 = Figure()
    axC4 = figC4.add_subplot(111)
    axC4.set_title('FC3')
    axC4.set_xlim(0, 100)
    axC4.set_ylim(-100000, 100000)
    axC4.tick_params(labelcolor='w', left=False)

    global linesC4
    linesC4 = axC4.plot([], [])[0]
    global canvasC4
    canvasC4 = FigureCanvasTkAgg(figC4, master=lblCanvas)
    canvasC4.get_tk_widget().place(x=0, y=250, width=750, height=50)
    canvasC4.draw()
    # CP3 6
    figCp3 = Figure()
    axCp3 = figCp3.add_subplot(111)
    axCp3.set_title('FC3')
    axCp3.set_xlim(0, 100)
    axCp3.set_ylim(-100000, 100000)
    axCp3.tick_params(labelcolor='w', left=False)

    global linesCp3
    linesCp3 = axCp3.plot([], [])[0]
    global canvasCp3
    canvasCp3 = FigureCanvasTkAgg(figCp3, master=lblCanvas)
    canvasCp3.get_tk_widget().place(x=0, y=300, width=750, height=50)
    canvasCp3.draw()
    # CPz 7
    figCpz = Figure()
    axCpz = figCpz.add_subplot(111)
    axCpz.set_title('FC3')
    axCpz.set_xlim(0, 100)
    axCpz.set_ylim(-100000, 100000)
    axCpz.tick_params(labelcolor='w', left=False)

    global linesCpz
    linesCpz = axCpz.plot([], [])[0]
    global canvasCpz
    canvasCpz = FigureCanvasTkAgg(figCpz, master=lblCanvas)
    canvasCpz.get_tk_widget().place(x=0, y=350, width=750, height=50)
    canvasCpz.draw()
    # CP4 8
    figCp4 = Figure()
    axCp4 = figCp4.add_subplot(111)
    axCp4.set_title('FC3')
    axCp4.set_xlim(0, 100)
    axCp4.set_ylim(-100000, 100000)
    axCp4.tick_params(labelcolor='w', left=False)

    global linesCp4
    linesCp4 = axCp4.plot([], [])[0]
    global canvasCp4
    canvasCp4 = FigureCanvasTkAgg(figCp4, master=lblCanvas)
    canvasCp4.get_tk_widget().place(x=0, y=400, width=750, height=40)
    canvasCp4.draw()

    # Button
    btnCon = Button(btnFrame, text=conf, command=confirm,
                    fg="blue", width=int(scrnWidth/100), height=int(scrnHeight/400))
    btnCon.grid(column=0, row=0, sticky="s")
    btnCon.config(font=("Arial", 18))
    lblBtn = LabelFrame(btnFrame, width=scrnWidth/8, borderwidth=0)
    lblBtn.grid(column=1, row=0, sticky='e')
    btnEx = Button(btnFrame, text=ex, command=exGui, fg="blue",
                   width=int(scrnWidth/100), height=int(scrnHeight/400))
    btnEx.grid(column=2, row=0, sticky='s')
    btnEx.config(font=("Arial", 18))

    # Decides the size of the screen
    root.geometry(f'{scrnWidth}x{scrnHeight}+{-10}+{0}')
    root.attributes("-fullscreen", True)

    ecs.activateEEG(user)
    root.after(1000, plot_data)
    root.mainloop()


def main():
    if __name__ == '__main__':
        initializeGui()


def updateGui(rooti):
    # Updates the previous GUI with this GUI
    global root
    root = rooti
    initializeGui()
