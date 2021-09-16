import serial
#from serial import Serial
#import time
ser = serial.Serial( port='COM12', baudrate=9600)
ser.close()
ser.open()
ser.write("*IDN?".encode())
#time.sleep(10)
ser.close()