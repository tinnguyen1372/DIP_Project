# Import packages needed
import socket
import twophase.solver  as sv
import twophase.start_server as ss
from threading import Thread


#Starting thread running socket server
port = 8080
max_move = 20
time_out = 2
server = Thread(target=ss.start, args=(port, max_move, time_out))
server.start()
