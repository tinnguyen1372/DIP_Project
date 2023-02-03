#!/usr/bin/env python3
import solver
import paho.mqtt.client as mqtt
from rubikscolorresolver.solver import RubiksColorSolverGeneric
import json

# This is the Subscriber
# Constant
max_length = 19
time_out = 2
#IP Address of the Broker (Bluetooth Network Connection)
ev3_ip = "192.168.137.137"

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("topic/ev3_to_pc")

def on_message(client, userdata, msg):
  dict = str(msg.payload.decode('utf-8'))
  cube = RubiksColorSolverGeneric(3)
  try:
    cube.enter_scan_data(json.loads(dict))
    cube.crunch_colors()
    output = "".join(cube.cube_for_kociemba_strict())
  except Exception as e:
    print(e)
    output = e
  cube = None
  cubestring = output
  method = 1 # 1 for Two phase Kociemba, 2 for Korf
  solution = solver.solve(max_length, time_out, cubestring, method)
  client.publish("topic/pc_to_ev3", solution)
  #client.disconnect()
    
client = mqtt.Client()
client.connect(ev3_ip,1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()