#!/usr/bin/env python3
import twophase.solver as sv
import paho.mqtt.client as mqtt
# This is the Subscriber
# Constant
max_length = 19
time_out = 2
#IP Address of the Broker (Bluetooth Network Connection)
ev3_ip = "169.254.193.219"

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("topic/ev3_to_pc")

def on_message(client, userdata, msg):
  cubestring = str(msg.payload.decode('utf-8'))
  print("Recieved scramble from EV3: {}".format(cubestring))
  print('Solving...')
  solution = sv.solve(cubestring,max_length,time_out)
  solution = solution[:solution.strip().rfind(" ")]
  print(solution)
  client.publish("topic/pc_to_ev3", solution)
  #client.disconnect()
    
client = mqtt.Client()
client.connect(ev3_ip,1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()