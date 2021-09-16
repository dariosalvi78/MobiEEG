import ast
import json

settings = {}


def loadSettings():
    file = open("settings/settings.txt", "r")
    global settings
    settings = json.load(file)
    file.close()


def saveSettings():
    global settings
    data = json.dumps(settings)
    # open file for writing
    file = open("settings/settings.txt", "w")
    # write file
    file.write(data)
    # close file
    file.close()
