import ast

settings = {}


def loadSettings():
    file = open("settings/settings.txt", "r")
    contents = file.read()
    global settings
    settings = ast.literal_eval(contents)
    file.close()
    print(settings)


def saveSettings():
    # open file for writing
    file = open("settings/settings.txt", "w")
    # write file
    file.write(str(dict))
    # close file
    file.close()
