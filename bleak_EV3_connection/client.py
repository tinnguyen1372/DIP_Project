#!/usr/bin/env pybricks-micropython
# Imagine we already scanned the rubik successfully and the results is a string like this:
# LLLLURRBDLFBDRRRULFUFFFRULDBUBDDFFBUUBUDLDDBRDFFUBLBRR

from pybricks.tools import wait

from usys import stdin, stdout
from uselect import poll
import asyncio

# register 
keyboard = poll()
keyboard.register(stdin)

while True:

    # # Optional: Check available input.
    # while not keyboard.poll(0):
    #     # Optional: Do something here.
    #     wait(10)
    
    # Code to get the scan result goes here: 

    scan_result = 'LLLLURRBDLFBDRRRULFUFFFRULDBUBDDFFBUUBUDLDDBRDFFUBLBRR'
    # Send the scan result to PC in byte string form:
    stdout.buffer.write(scan_result.encode())
    # Read the whole stream response
    cmd = stdin.buffer.read()
    # Check if the result is good:
    print("The solving steps are: ", cmd)
    # Decide what the hardware needs to do based on the command:
    
    
    # Send a response.
    stdout.buffer.write(b"Received ", cmd)