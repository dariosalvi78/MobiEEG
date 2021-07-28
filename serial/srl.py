# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 14:13:19 2021

@author: Veronica
"""

import serial
import time
puerto = serial.Serial(port= 'COM13', baudrate = 9600)
puerto.write("a".encode())
time.sleep(1)
puerto.close()
