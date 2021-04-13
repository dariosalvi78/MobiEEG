import datetime
global temp
temp = datetime.datetime.now()
#channeldatas
global fileNameData
fileNameData = (str(temp.year) + str(temp.month) + str(temp.day)  
    + '-' + str(temp.hour) + ';'+ str(temp.minute) + '-data')
createFileData = open("Reports\{}.csv".format(fileNameData), "w")
createFileData.close()
global fileWriterData
fileWriterData = open("Reports\{}.csv".format(fileNameData), "w")
fileWriterData.writelines("Time\t\tFC3,FCZ,FC4,C3 ,Cz ,C4 ,CP3,CPz,CP4\n")

fileNameEvent = (str(temp.year) + str(temp.month) + str(temp.day)  
    + '-' + str(temp.hour)+ ';'+ str(temp.minute) + '-events')
createFileEvent = open("Reports\{}.csv".format(fileNameEvent), "w")
createFileEvent.close()
global fileWriterEvent 
fileWriterEvent = open("Reports\{}.csv".format(fileNameEvent), "w")
fileWriterEvent.writelines("Patient:\t" + "user" + "\n")
fileWriterEvent.writelines("Date and Time:\t" + str(datetime.datetime.now()) + "\n")
fileWriterEvent.writelines("Pain level:\t" + str(34) + "\n\n")

