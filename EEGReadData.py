import random

def readFc3(cond):
    if cond == True:
        fc3 = rand()
        return fc3
    elif cond == False:
        return -5

def readFcz(cond):
    if cond == True:
        fcz = rand()
        return fcz
    elif cond == False:
        return -5
    
def readFc4(cond):
    if cond == True:
        fc4 = rand()
        return fc4
    elif cond == False:
        return -5

def readC3(cond):
    if cond == True:
        c3 = rand()
        return c3
    elif cond == False:
        return -5

def readCz(cond):
    if cond == True:
        cz = rand()
        return cz
    elif cond == False:
        return -5

def readC4(cond):
    if cond == True:
        c4 = rand()
        return c4
    elif cond == False:
        return -5

def readCp3(cond):
    if cond == True:
        cp3 = rand()
        return cp3
    elif cond == False:
        return -5

def readCpz(cond):
    if cond == True:
        cpz = rand()
        return cpz
    elif cond == False:
        return -5

def readCp4(cond):
    if cond == True:
        cp4 = rand()
        return cp4
    elif cond == False:
        return -5

def rand():
    return random.randint(0,256)

def checkSignal(channel):

    if channel == 0:
        # check th signal from fc3 from the SDK python
        # connction = signalFC3()
        connection = True
        return connection
    elif channel == 1:
        # connction = signalFCz()
        connection = True
        return connection
    elif channel == 2:
        # connction = signalFC4()
        connection = True
        return connection
    elif channel == 3:
        # connction = signalC3()
        connection = True
        return connection
    elif channel == 4:
        # connction = signalCz()
        connection = True
        return connection
    elif channel == 5:
        # connction = signalC4()
        connection = True
        return connection
    elif channel == 6:
        # connction = signalCPz()
        connection = True
        return connection
    elif channel == 7:
        # connction = signalCP4()
        connection = True
        return connection
    elif channel == 8:
        # connction = signalCP3()
        connection = True
        return connection

def getData(channel, connection):
    if channel == 0:
        # get data from channel FC3
        data = readFc3(connection)
        return data
    elif channel == 1:
        # get data from channel FCz
        data = readFcz(connection)
        return data
    elif channel == 2:
        # get data from channel FC4
        data = readFc4(connection)
        return data
    elif channel == 3:
        # get data from channel C3
        data = readC3(connection)
        return data
    elif channel == 4:
        # get data from channel Cz
        data = readCz(connection)
        return data
    elif channel == 5:
       # get data from channel C4
        data = readC4(connection)
        return data
    elif channel == 6:
        # get data from channel CP3
        data = readCp3(connection)
        return data
    elif channel == 7:
        # get data from channel CPz
        data = readCpz(connection)
        return data
    elif channel == 8:
        # get data from channel CP4
        data = readCp4(connection)
        return data