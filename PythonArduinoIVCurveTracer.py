# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 08:36:29 2021

@author: cosmi
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 07:40:42 2021

@author: cosmi
"""

import serial # import from pySerial
import numpy as np # import library from Numerical python
import matplotlib.pyplot as plt # import Library from matplotlib
from drawnow import drawnow # import lib from drawnow
import matplotlib.animation as animation

X = [] # create an empty array for graphing
Y = []
# set up serial connection with    arduino
ser = serial.Serial(
    port='COM7',
    baudrate=9800)

#ser.flushInput() # optional

plt.ion() # tell matplotlib you want interactive mode to plot data
cnt = 0

def makeFig(): # create a function to make plot
    #plt.ylim(2500,3000)     
    #fig = plt.figure()
    #ax = fig.add_subplot(1, 1, 1)                            #Set y min and max values
    plt.title('My Live Streaming Sensor Data')      #Plot the title
    plt.grid(True)                                  #Turn the grid on
    plt.ylabel('Current (mA)')  
    plt.xlabel('Voltage Drop (uV)')                          #Set xlabels
    plt.plot(X,Y, 'ro', label='IV trace')       #plot the temperature
    plt.legend(loc='upper left')                    #plot the legend
    #plt2=plt.twinx()                                #Create a second y axis
    plt.ylim(-20000,20000)                           #Set limits of second y axis- adjust to readings you are getting
    plt.xlim(2000,6000)
    #plt.set_xlabel('Voltage (uV)')                    #label second y axis
    plt.ticklabel_format(useOffset=False)           #Force matplotlib to autoscale y-axis
    plt.legend(loc='upper right')                  #plot the legend
    

while True: # loop that lasts forever
    #ser.write(str.encode('10')) #write data to the port to request the random number. 

    while (ser.inWaiting()==0): # wait till there is data to plot
         pass # do nothing

    arduinoString =ser.readline()
    string = arduinoString.decode()  # convert the byte string to a unicode string
    pystring = string.strip() # remove the characters
    printstring = (pystring)
    print(printstring)
    dataArray = printstring.split(',')   #Split it into an array called dataArray

    x = float(dataArray[0])            #Convert first element to floating number and put in temp
    y = float(dataArray[1])            #Convert second element to floating number and put in P
 
    X.append(x)                     #Build our array by appending x readings
    Y.append(y)                     #Building our array by appending y readings
    drawnow(makeFig)                       #Call drawnow to update our live graph
    plt.pause(.000001)                     #Pause Briefly. Important to keep drawnow from crashing
    cnt=cnt+1
    #if(cnt>50):                            #If you have 50 or more points, delete the first one from the array
    #    X.pop(0)                       #This allows us to just see the last 50 data points
    #    Y.pop(0)