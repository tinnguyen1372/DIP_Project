#!/usr/bin/env python3
from sys import stderr
import paho.mqtt.client as mqtt
from ev3dev2.sound import Sound
from sys import stderr
import os

sound = Sound()
sound.beep()
cubestring = 'DUUBULDBFRBFRRULLLBRDFFFBLURDBFDFDRFRULBLUFDURRBLBDUDL'

def on_connect(client, userdata, flags, rc):
    client.subscribe("topic/pc_to_ev3")

def on_message(client, userdata, msg):
    message = str(msg.payload.decode('utf-8'))
    print('Received Solution from PC: {}'.format(message), file=stderr)
    client.disconnect()

client = mqtt.Client()
client.connect("localhost",1883,60)
client.publish("topic/ev3_to_pc", cubestring)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()