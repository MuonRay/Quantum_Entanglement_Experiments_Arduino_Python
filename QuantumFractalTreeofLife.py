# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 00:57:36 2021

@author: cosmi
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 04:10:06 2021

@author: cosmi

pip install pygame for graphics
"""

import pygame
from pygame.draw import line	
from math import sin,cos,radians
import time

import random

#pip install pyserial

import serial
'''there are at least 3 things we can randomise here: branch length, angle and turn angle

Branch length is easy to radnomise, we can select a random int between a set branch length
You could play the same trick to randomize the angle. This is harder because you need 
to be able to undo the angle and it would be good if the left and right angles were 
not identical. One way to solve this would be to add a variable and break up the turn 
between the two branches into two separate turns.


Create a new angle variable and set it equal to your base angle (currently 45) 
plus some random amount between -45 and +45

Rather than the 90 degree turn to the right, 
turn right by this angle to undo the left turn

Immediately after this right turn, calculate a new random angle

Use this angle to turn right

After drawing the second smaller tree, use the new angle to turn left 
'''


pygame.init()

HIGHT,WITDH = 700,800


BLACK =(0,0,0)
WHITE =(255,255,255)
BLUE  =(0,0,255)
RED   =(255,0,0)

surface = pygame.display.set_mode((WITDH,HIGHT))


def ftree(pos,length,rndnums,angle,turn_angle,depth,color,split):
	if depth==0:
		return
	x,y=pos
	new_x= x+ cos(radians(angle))*length 
	new_y= y- sin(radians(angle))*length
	line(surface,color,pos,(int(new_x),int(new_y)))

	new_pos = (new_x,new_y)
    #rndnums to int
	length= 0.7*length  #make this part random using the quantum random numbers
    
	color1=color2=color
	if split:
		color1=BLUE
		color2=RED
	ftree(new_pos, length, rndnums, angle, turn_angle, depth-1, color1,False)
	ftree(new_pos, length, rndnums, angle, turn_angle, depth-1, color2,False)



#variables
angle = 90 # for initial angle
length = 100 #start length
turn_angle=0   
depth = 4 # number of recursions
INIT_POS = (WITDH//2,HIGHT)
quantum_random = 0
rndnums = 0
#arduino connection, make sure the COM# is correct.
#ser = serial.Serial('COM7', 9800, timeout=1)
#ser.flushInput()
#time.sleep(2)
ser = serial.Serial(
    port='COM7',
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
    
    surface.fill(BLACK)
    ftree(INIT_POS,length,rndnums,angle,turn_angle,depth,WHITE,True)	
    turn_angle=rndnums # random bloch sphere angles (arctangent of H and V modes)
    pygame.display.update()
    