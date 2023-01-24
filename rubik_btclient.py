"""
A simple Python script to send messages to a sever over Bluetooth
using PyBluez (with Python 2).
"""

import bluetooth

serverMACAddress = '34:E1:2D:86:D8:22'
port = 2
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.connect((serverMACAddress, port))
while 1:
    text = input() # Note change to the old (Python 2) raw_input
    if text == "quit":
        break
    s.send(text)
s.close()
