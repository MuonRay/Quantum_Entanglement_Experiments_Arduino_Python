# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 01:57:21 2021

@author: cosmi
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 00:57:36 2021

@author: cosmi
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 04:10:06 2021

@author: cosmi

python to arduino random number interface


"""

#pip install pyserial

import serial

#arduino connection, make sure the COM# is correct.
#ser = serial.Serial('COM7', 9800, timeout=1)
#ser.flushInput()
#time.sleep(2)
ser = serial.Serial(
    port='COM8',
    baudrate=9800,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=1)

RUN  = True

while RUN:
    ser.write(str.encode('r')) #write data to the port to request the random number. 
    ser_bytes = ser.readline()   # read a byte string

    #Let's sum up the data type conversions above. Starting from the data that comes 
    #in from the Arduino that is a byte to finally ending up with an integer:

    #ser.readline() returns a byte string: b'1\r\n'
    #.decode() converts the byte string to a Python string: '1\r\n'
    #.strip() removes the \r\n characters from the end of the Python string: '481'
    #int() converts the Python string to an integer: the random number we use
    
    string = ser_bytes.decode()  # convert the byte string to a unicode string
    pystring = string.strip() # remove the characters
    printstring = (pystring)
    print(printstring)
    rndnums = printstring
    quantum_angle = 0
    #string1 = ser_bytes.decode()  # convert the byte string to a unicode string
    #rndnums = int(string1) # convert the unicode string to an int
    #quantum_angle=string1
    #print(rndnums)