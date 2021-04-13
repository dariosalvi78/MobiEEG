import requests
from websocket import create_connection
import json
import datetime
import time
import math

# Login:


def logIn(ema, passw):
    connection = False
    try:
        loginPost = requests.post('http://localhost:3000/api/login', json={
            'email': ema,
            'password': passw
        })
        loginInfo = json.loads(loginPost.text)
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

    
#def sendDataToServer():


# con = logIn('john.doe@test.test', 'outerZpace')
# print(con)