import requests
from websocket import create_connection
import json
import datetime
import time
import math

# Login:


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
    timedelta = (datetime.datetime.now())
    x = {"ts": str(timedelta.hour) +":" + str(timedelta.minute) + ":" + str(timedelta.second),
        "events": eve,
        "details": det
        }
    ws.send(json.dumps(x))

#def sendDataToServer():


# con = logIn('john.doe@test.test', 'outerZpace')
# print(con)