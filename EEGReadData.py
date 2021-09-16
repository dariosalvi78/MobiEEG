'''
Searching and connecting to the EEG device, a thread is running and...
this connection runs until a boolean stops it. 
@uthor Rohan Samandari
'''

from bbt import Device
import Settings
import EEGToCSV as ecs
import MobiClient as mc
import time
import datetime


chann0 = chann1 = chann2 = chann3 = chann4 = chann5 = chann6 = chann7 = chann8 = 0
instructionBegin = False
connection = False
mainConnection = True
timeStamp = datetime.datetime.now()
chImp0 = chImp1 = chImp2 = chImp3 = chImp4 = chImp5 = chImp6 = chImp7 = chImp8 = "ImpedanceLevel.UNKNOWN"


def try_to(condition, action, tries, message=None):
    # This method works for connectin /Rohan
    # Trys to do an action which is received from other methods.
    t = 0
    global threadStop
    while (not condition() and t < tries and mainConnection):
        t += 1
        if message:
            print("{} ({}/{})".format(message, t, tries))
        action()
    return condition()


def setMainConnection():
    # This method kills the thread which is running the connection, by seting the while loop to False
    global mainConnection
    mainConnection = False


def setMainConnectionTrue():
    # Runs the tread which is running the connection again when needed.
    global mainConnection
    mainConnection = True


def connectToEEG():
    # This method works for connecting the device and running the data received from the device
    # Connecting only to one device which is called "BBT-SMT-AAA011"
    # name is only use with the bluetooth conextion.
    name = Settings.settings['deviceName']
    # portCOM is the USB port
    portCOM = Settings.settings['devicePortNumber']
    global device, connection, mainConnection

    with Device.create_usb_device(portCOM) as device:
        # with Device.create_bluetooth_device(name) as device:
        if not try_to(device.is_connected, device.connect, 5, "Connecting to {}".format(name)):
            print("unable to connect")
        else:
            connection = True
            signals = device.get_signals()
            for s in signals:
                s.set_mode(1)

            device.start()
            firstPacket = True
            packetTs = 0
            seqN = 0
            while(mainConnection):
                sequence, battery, flags, data = device.read()
                if(instructionBegin == False):
                    time.sleep(0.01)
                    setImpedanceLevel(device.get_eeg_impedance(0), device.get_eeg_impedance(1),
                                      device.get_eeg_impedance(2), device.get_eeg_impedance(
                                          3), device.get_eeg_impedance(4), device.get_eeg_impedance(5),
                                      device.get_eeg_impedance(6), device.get_eeg_impedance(7), device.get_eeg_impedance(8))
                if(instructionBegin == True):
                    if (firstPacket == True):
                        packetTs = datetime.datetime.now()
                        seqN = sequence
                        firstPacket = False
                    else:
                        packetTs = packetTs + \
                            datetime.timedelta(microseconds=(
                                31250 * (sequence - seqN)))
                        seqN = sequence
                for i in range(0, 8):
                    if(instructionBegin == True):
                        ts = packetTs + \
                            datetime.timedelta(microseconds=(3906 * i))
                        setTS(ts)
                        ecs.writeToFile(ts, data[i], data[i+8], data[i+16], data[i+24],
                                        data[i+32], data[i+40], data[i+48], data[i+56], data[i+64])
                        mc.sendDataToServer(ts, data[i], data[i+8], data[i+16], data[i+24],
                                            data[i+32], data[i+40], data[i+48], data[i+56], data[i+64])
                    else:
                        setData(data[i], data[i+8], data[i+16], data[i+24], data[i+32],
                                data[i+40], data[i+48], data[i+56], data[i+64])
            device.disconnect()


def setData(ch0, ch1, ch2, ch3, ch4, ch5, ch6, ch7, ch8):
    # Receives data from EEGs 9 channels and sets it to global variables there the other classes can reach them
    global chann0, chann1, chann2, chann3, chann4, chann5, chann6, chann7, chann8, chann9
    chann0 = ch0
    chann1 = ch1
    chann2 = ch2
    chann3 = ch3
    chann4 = ch4
    chann5 = ch5
    chann6 = ch6
    chann7 = ch7
    chann8 = ch8


def setTS(ts):
    global timeStamp
    timeStamp = ts

# def led():
#    puerto = serial.Serial(port= 'COM14', baudrate = 9600)
#    puerto.write("a".encode())
#    puerto.close()


def led():
    import serial
    import time
    puerto = serial.Serial(port='COM13', baudrate=9600)
    puerto.write("a".encode())
    # time.sleep(1)
    puerto.close()


def getTimeStamp():
    global timeStamp
    return timeStamp


def getData():
    # Sends the data from receiver
    global chann0, chann1, chann2, chann3, chann4, chann5, chann6, chann7, chann8
    return chann0, chann1, chann2, chann3, chann4, chann5, chann6, chann7, chann8


def setImpedanceLevel(ch0, ch1, ch2, ch3, ch4, ch5, ch6, ch7, ch8):
    # Receives the level of connection signals for each channel and set them to global variables
    global chImp0, chImp1, chImp2, chImp3, chImp4, chImp5, chImp6, chImp7, chImp8
    chImp0 = str(ch0)
    chImp1 = str(ch1)
    chImp2 = str(ch2)
    chImp3 = str(ch3)
    chImp4 = str(ch4)
    chImp5 = str(ch5)
    chImp6 = str(ch6)
    chImp7 = str(ch7)
    chImp8 = str(ch8)


def getImpedanceLevel():
    # Sends the connection signals of each channel
    global chImp0, chImp1, chImp2, chImp3, chImp4, chImp5, chImp6, chImp7, chImp8
    return chImp0, chImp1, chImp2, chImp3, chImp4, chImp5, chImp6, chImp7, chImp8


def setSendTrue():
    # Receives information about that the instruction has begun
    global instructionBegin
    instructionBegin = True


def capConnected():
    # Sends infromation about if the EEG device is connected
    global connection
    return connection

# Done
