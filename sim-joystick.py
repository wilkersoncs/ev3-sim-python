#!/usr/bin/env python3

# imports
#------------
# import log function
from ev3devlogging import timedlog as log
import pygame, sys
pygame.init()
# import ev3 API
from ev3dev2 import auto as ev3
pyjoy = pygame.joystick.Joystick(0)
pyjoy.init()

# initialize
#------------
# initialize left and right motor as tank combo
tankDrive = ev3.MoveTank(ev3.OUTPUT_A, ev3.OUTPUT_D)

SPEED_FORWARD = ev3.SpeedPercent(30)     # set speed to 30% of maximum speed
SPEED_BACKWARD = ev3.SpeedPercent(-30)   # backward with same speed as forward
SPEED_ZERO   = ev3.SpeedPercent(0)       # stop motor (speed is zero)

TURN_TIME=0.62
log("Ready to drive")

while True:
    for event in pygame.event.get():
        log(event)

        if pyjoy.get_axis(1) < -.5:
            log("drive forward")
            tankDrive.on_for_seconds(SPEED_FORWARD, SPEED_FORWARD, 1)
        if pyjoy.get_axis(1) > .5:
            log("drive backward")
            tankDrive.on_for_seconds(SPEED_BACKWARD, SPEED_BACKWARD, 1)
        if pyjoy.get_axis(0) > .5:
            log("right turn")
            tankDrive.on_for_seconds(SPEED_FORWARD, SPEED_BACKWARD, TURN_TIME)
        if pyjoy.get_axis(0) < -.5:
            log("left turn")
            tankDrive.on_for_seconds(SPEED_BACKWARD, SPEED_FORWARD, TURN_TIME)
        
