'''
Log in to Mobistudey server with a Mobistudy account
'''
import requests
from websocket import create_connection
import json
import datetime
import time
import math
import struct

timeBegin = datetime.datetime.now()

def logIn(ema, passw):
    return True
# Loging in with receieved userName and password
# Returns a boolean about the succeed of the login process
    try:
        loginPost = requests.post('http://192.168.224.118:3000/api/login', json={
            'email': ema,
            'password': passw
        })
        loginInfo = json.loads(loginPost.text)
        global ws
        ws = create_connection("ws://192.168.224.118:3000/api/live/eeg")
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
    return True
# Sends event from the task instruction to the server as a json file
    global ws
    global timeBegin
    # timedelta = (datetime.datetime.now())
    timedelta = (datetime.datetime.now() - timeBegin)
    x = {
        "ts": math.floor(timedelta.total_seconds()*1000000),
        "event": eve,
        "details": det
        }
    ws.send(json.dumps(x))

def sendDataToServer(ts, fc3, fcz, fc4, c3, cz, c4, cp3, cpz, cp4):
    return True
# Receives data from each channel and sends them to the server as a json file
    global timeBegin

    timedelta = (ts - timeBegin)
    bytes = (math.floor(timedelta.total_seconds() * 1000000)
        ).to_bytes(4, byteorder='little', signed=False)

    bytes = bytes + bytearray(struct.pack("f", fc3))
    bytes = bytes + bytearray(struct.pack("f", fcz))
    bytes = bytes + bytearray(struct.pack("f", fc4))
    bytes = bytes + bytearray(struct.pack("f", c3))
    bytes = bytes + bytearray(struct.pack("f", cz))
    bytes = bytes + bytearray(struct.pack("f", c4))
    bytes = bytes + bytearray(struct.pack("f", cp3))
    bytes = bytes + bytearray(struct.pack("f", cpz))
    bytes = bytes + bytearray(struct.pack("f", cp4))

    ws.send_binary(bytes)

def setTime():
    global timeBegin
    timeBegin = datetime.datetime.now()

def closeConnection():
    return True
    global ws
    ws.close()
'''
john.doe@test.test
outerZpace
'''
#Done