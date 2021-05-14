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
    # Loging in with receieved userName and password
    # Returns a boolean about the succeed of the login process
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
    # Sends event from the task instruction to the server as a json file
    global ws
    global timeBegin
    # timedelta = (datetime.datetime.now())
    timedelta = (datetime.datetime.now() - timeBegin)
    x = {
        # time is in milliseconds since start
        "ts": math.floor(timedelta.total_seconds() * 1000),
        "events": eve,
        "details": det
    }
    ws.send(json.dumps(x))


def sendDataToServer(ts, fc3, fcz, fc4, c3, cz, c4, cp3, cpz, cp4):
    # Receives data from each channel and sends them to the server as a json file

    # timedelta = datetime.datetime.now()
    # global end
    global timeBegin

    timedelta = (ts - timeBegin)
    bytes = (math.floor(timedelta.total_seconds() * 1000)  # time is in milliseconds since start
             ).to_bytes(4, byteorder='little', signed=False)
    # bytes = (datetime.datetime.now()).to_bytes(4, byteorder='little', signed=False)
    # then we send 9 samples of unsigned 32 bits integers

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
    global ws
    ws.close()


'''
john.doe@test.test
outerZpace
'''
# Done
