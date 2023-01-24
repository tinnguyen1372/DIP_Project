"""
A simple Python script to receive messages from a client over
Bluetooth using PyBluez (with Python 2).
"""

import bluetooth

hostMACAddress = '34:E1:2D:86:D8:22' # The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
port = 2
backlog = 1
size = 1024
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.bind((hostMACAddress, port))
s.listen(backlog)
print("Server is listening")
try:
    client, clientInfo = s.accept()
    print("Accept connections from: {}".format(client))
    while 1:
        data = client.recv(size)
        if data:
            print(data)
            client.send(data) # Echo back to client
except:	
    print("Closing socket")
    client.close()
    s.close()