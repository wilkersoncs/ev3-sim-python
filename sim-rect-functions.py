#!/usr/bin/env python3

# imports
#------------
# import log function
from ev3devlogging import timedlog as log
# import ev3 API
from ev3dev2 import auto as ev3

def turn_right():
    log("turn right")
    tankDrive.on_for_seconds(SPEED_FORWARD, SPEED_BACKWARD,TURN_TIME)

def turn_left():
    log("turn left")
    tankDrive.on_for_seconds(SPEED_BACKWARD, SPEED_FORWARD, TURN_TIME)

def drive_forward(seconds):
    log("drive forward %d" %seconds)
    #log(seconds)
    tankDrive.on_for_seconds(SPEED_FORWARD, SPEED_FORWARD, seconds)

    
# initialize
#------------
# initialize left and right motor as tank combo
tankDrive = ev3.MoveTank(ev3.OUTPUT_A, ev3.OUTPUT_D)

# initialize some constants
SPEED_FORWARD = ev3.SpeedPercent(30)     # set speed to 30% of maximum speed
SPEED_BACKWARD = ev3.SpeedPercent(-30)   # backward with same speed as forward
SPEED_ZERO   = ev3.SpeedPercent(0)       # stop motor (speed is zero)

TURN_TIME=0.62

# main loop
#-----------
drive_forward(1)
turn_right()
drive_forward(3)
turn_left()
drive_forward(1)
turn_left()
turn_left()
#turn_right()
drive_forward(1)
turn_right()
drive_forward(3)
turn_right()
log("finished")
