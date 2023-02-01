#!/usr/bin/env python3

import paho.mqtt.client as mqtt
from ev3dev2.sound import Sound

sound = Sound()
sound.beep()
# This is the Publisher

client = mqtt.Client()
client.connect("localhost",1883,60)
client.publish("topic/test", "Hello world!")
client.disconnect()