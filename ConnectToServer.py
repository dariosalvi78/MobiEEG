# This wait page is only going to be shown while the application is connecting to the server
# Author: Rohan
 
from tkinter import *
root =Tk()
user = None
    
def vas():
    import VAS
    root.destroy()
    VAS.initializeGui()
    # root.after(1000, vas)


def initializeGui():

    readFile = open("LanguageSettings\ChosenLanguage.txt", "r")
    temp = readFile.readlines()
    temp1 = temp[0]
    chosenLang = open("LanguageSettings\{}.txt".format(temp1), "r", encoding='utf-8')
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

    lblTitel = LabelFrame(root, text= frTitle, padx=scrnWidth/160, pady=scrnHeight/30, border=2)
    lblTitel.grid(column=1, row=0, padx=scrnWidth/12, pady= scrnHeight/8, ipadx=scrnWidth/30, sticky="s")
    

        #Decides the size of the screen 
    root.geometry(f'{800}x{300}+{posR-200}+{posD}')
    root.after(1000, vas)
    root.attributes("-fullscreen", False)
    root.mainloop()


def main():
    if __name__ == '__main__':
        initializeGui()
    
main()