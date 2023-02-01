#!/usr/bin/env python3

from time import sleep
import os
from sys import stderr
from ev3dev2.led import Leds
from ev3dev2.sound import Sound

##Setup
sound = Sound()
os.system('setfont Lat15-TerminusBold14')
leds = Leds()

##Begin 
sound.speak('Hello, my name is EV3')
print('Program Starting', file=stderr) 

## print to VS Code output panel
print('EV3 DIP rules!')
print()  # print a blank line
sleep(5) 

## LED Show
leds.all_off() # Turn all LEDs off
sleep(1)

# Set both pairs of LEDs to amber
leds.set_color('LEFT', 'AMBER')
leds.set_color('RIGHT', 'AMBER')
sleep(4)

# With custom colors:
leds.set_color('LEFT', (1, 0)) # Bright Red.
leds.set_color('RIGHT', (0, 1)) # Bright green.
sleep(4)
leds.all_off() # Turn all LEDs off