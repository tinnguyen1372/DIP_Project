#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time
from pprint import pformat
from time import sleep
import json
import logging
import os
import signal
import sys

"""
This script is just a demo on how pybricks works.
You should have the ev3 micropython extension on your VSCode in order to run this directly from your VSCode to load on your EV3 Brick.
For function calls to control sensors and motors, refer to https://docs.pybricks.com/en/latest/.
"""

# Create your objects here.
# Initialize the EV3 brick.
ev3 = EV3Brick()

color = ColorSensor(Port.S2) # Color sensor, to scan the cube colors
set_turn = UltrasonicSensor(Port.S1) # Ultrasonic sensor, to detect whether cube is present
move_sensor = Motor(Port.C) # Motor used to move the color sensor
rotate = Motor(Port.B) # Motor used to rotate platform
turn = Motor(Port.A) # Motor used to move the arm

move_sensor.run_time(1000, 2500, wait=True) # Run motor by 1000 speed unit for 2500ms, reset position of sensor motor
rotate.run_time(-500, 2500, wait=True) # Reset rotating arm motor
rotate.run_target(500, 5, wait=True)
turn.run(-250)
while True:
    if turn.angle() > -15:
        turn.stop()
        break

move_sensor.run_target(500, 216, wait=True) # Run move sensor to read top value

color_name = color.color() # returns a color name
color_rgb = color.rgb() # returns a tuple of R, G and B reflected values as percentage
print("Scanned color name: ", color_name, "Scanned color RGB values: ", color_rgb)

        

