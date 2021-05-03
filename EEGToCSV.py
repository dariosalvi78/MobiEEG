'''
Creats csv file and stores the data received from EEG device. 
@uthor Rohan Samandari
'''
import datetime
# import EEGReadData as erd
import csv

def getFileWriterEvent():
# Sends the filewriter for events
    global fileWriterEvent
    return fileWriterEvent

def getFileWriterData():
#Sends the filewriter for data
    global fileWriterData
    return fileWriterData

def createCSVFile():
# Creates csv files for data and events

    global temp, user, fileNameData
    temp = datetime.datetime.now()
    fileNameData = (str(temp.year) + str(temp.month) + str(temp.day)  
        + '-' + str(temp.hour) + ';'+ str(temp.minute) + '-data')
    createFileData = open("Reports\{}.csv".format(fileNameData), "w")
    createFileData.close()
    global fileWriterData
    fileWriterData = open("Reports\{}.csv".format(fileNameData), "w", newline='')
    fileWriterData.writelines("Time\t\t,FC3,FCZ,FC4,C3 ,Cz ,C4 ,CP3,CPz,CP4\n")
    
    fileNameEvent = (str(temp.year) + str(temp.month) + str(temp.day)  
        + '-' + str(temp.hour)+ ';'+ str(temp.minute) + '-events')
    createFileEvent = open("Reports\{}.csv".format(fileNameEvent), "w")
    createFileEvent.close()
    global fileWriterEvent 
    fileWriterEvent = open("Reports\{}.csv".format(fileNameEvent), "w", newline='')
    fileWriterEvent.writelines("Patient:, " + user + ", " + ", \n")
    fileWriterEvent.writelines("Date and Time:, " + str(datetime.datetime.now()) +",   ,\n")
    fileWriterEvent.writelines("Pain level:, " + str(painLevel) + ", \t, \n\n")

def writeToFile(fc3, fcz, fc4, c3, cz, c4, cp3, cpz, cp4):
# Receives data from each channels ans stores them to the csv file
    temp = datetime.datetime.now()
    time = str(temp.hour) +':'+ str(temp.minute)+':' + str(temp.second)+':'+str(temp.microsecond)
    
    sgnlWriter = csv.writer(fileWriterData, delimiter=',', quotechar='"', 
    quoting=csv.QUOTE_MINIMAL)
    sgnlWriter.writerow([time, str(fc3), str(fcz),
    str(fc4), str(c3), str(cz), str(c4), str(cp3),
    str(cpz), str(cp4)])

def activateEEG(userName):
# Receives and Sets the username and runs the create files method
    global user
    user = userName
    createCSVFile()

def setVAS(vas):
# Receives and sets the pain level
    global painLevel
    painLevel = vas

#Done



    