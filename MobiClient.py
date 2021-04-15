import requests
from websocket import create_connection
import json
import datetime
import time
import math


# Login:
timeBegin = datetime.datetime.now()
# end = True

def logIn(ema, passw):
    try:
        loginPost = requests.post('http://localhost:3000/api/login', json={
            'email': ema,
            'password': passw
        })
        loginInfo = json.loads(loginPost.text)
        global ws
        ws = create_connection("ws://localhost:3000/api/live/eeg")

        startTS = datetime.datetime.now()

        # send init information
        x = {
            "token": loginInfo["token"],
            "startTS": startTS.isoformat(),
            "studyKey": 10101,
            "taskId": 2
        }
        ws.send(json.dumps(x))
        return True
    except:
        return False

def sendEvent(eve, det):
    global ws
    global timeBegin
    # timedelta = (datetime.datetime.now())
    timedelta = (datetime.datetime.now() - timeBegin)
    x = {
        "ts": math.floor(timedelta.total_seconds()*1000),
        #Time as time if Dario wnats it
        # "ts": str(timedelta.hour) +":" + str(timedelta.minute) + ":" + str(timedelta.second),
        "events": eve,
        "details": det
        }
    ws.send(json.dumps(x))

def sendDataToServer(fc3, fcz, fc4, c3, cz, c4, cp3, cpz, cp4):
    # timedelta = datetime.datetime.now()
    # global end
    global timeBegin

    # if(end == True):
    timedelta = (datetime.datetime.now() - timeBegin)
    bytes = (math.floor(timedelta.total_seconds() * 1000)
        ).to_bytes(4, byteorder='little', signed=False)
    # bytes = (datetime.datetime.now()).to_bytes(4, byteorder='little', signed=False)
    bytes = bytes + (fc3).to_bytes(4, byteorder='little', signed=False)
    bytes = bytes + (fcz).to_bytes(4, byteorder='little', signed=False)
    bytes = bytes + (fc4).to_bytes(4, byteorder='little', signed=False)
    bytes = bytes + (c3).to_bytes(4, byteorder='little', signed=False)
    bytes = bytes + (cz).to_bytes(4, byteorder='little', signed=False)
    bytes = bytes + (c4).to_bytes(4, byteorder='little', signed=False)
    bytes = bytes + (cp3).to_bytes(4, byteorder='little', signed=False)
    bytes = bytes + (cpz).to_bytes(4, byteorder='little', signed=False)
    bytes = bytes + (cp4).to_bytes(4, byteorder='little', signed=False)

    ws.send_binary(bytes)
    # else:
    #     ws.close()

def setTime():
    global timeBegin
    timeBegin = datetime.datetime.now()

# def StopSendDataToServer():
#     global end
#     end = False

def SendPainLevel(pain):
    # global ws
    painLevel = str(pain) 
    timedelta = datetime.datetime.now()
    x = {
        # "ts": math.floor(timedelta.total_seconds()*1000),
        #Time as time if Dario wnats it
        "ts": str(timedelta.hour) +":" + str(timedelta.minute) + ":" + str(timedelta.second),
        "events": "Pain Level",
        "details": painLevel
        }
    ws.send(json.dumps(x))

# con = logIn('john.doe@test.test', 'outerZpace')
# print(con)