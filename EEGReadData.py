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