# basic example of sending data with python
# this example is vrey basic and doesn't handle disconnections or multi threading!
# check https://pypi.org/project/websocket-client/ for more advanced cases

import requests
from websocket import create_connection
import json
import datetime
import time
import math

# Login:
loginPost = requests.post('http://localhost:3000/api/login', json={
    'email': 'john.doe@test.test',
    'password': 'outerZpace'
})
loginInfo = json.loads(loginPost.text)
print(loginPost.text)



# websocket.enableTrace(True)
ws = create_connection("ws://localhost:3000/api/live/eeg")
print(ws)

startTS = datetime.datetime.now()

# send init information
x = {
    "token": loginInfo["token"],
    "startTS": startTS.isoformat(),
    "studyKey": 10101,
    "taskId": 2
}
ws.send(json.dumps(x))
print(json.dumps(x))

time.sleep(1)

# send event
timedelta = (datetime.datetime.now() - startTS)
x = {
    "ts": math.floor(timedelta.total_seconds() * 1000),
    "event": "LA",
    "details": "Left arrow started"
}
ws.send(json.dumps(x))
print(json.dumps(x))


time.sleep(1)

# send EEG
timedelta = (datetime.datetime.now() - startTS)
# first 4 bytes are the time passed since start in ms
bytes = (math.floor(timedelta.total_seconds() * 1000)
         ).to_bytes(4, byteorder='little', signed=False)

# then we send 9 samples of unsigneed 32 bits integers
for i in range(9):
    bytes = bytes + (2000 + i).to_bytes(4, byteorder='little', signed=False)

ws.send_binary(bytes)


ws.close()
