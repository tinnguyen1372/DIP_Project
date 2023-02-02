#!/usr/bin/env python3
from sys import stderr
import paho.mqtt.client as mqtt
from ev3dev2.sound import Sound
from sys import stderr
import os

sound = Sound()
sound.beep()
cubestring = '{"13": [200, 212, 78], "51": [129, 43, 16], "23": [172, 74, 13], "24": [9, 122, 138], "21": [2, 125, 141], "29": [243, 252, 249], "25": [10, 51, 175], "52": [103, 3, 1], "16": [203, 215, 81], "2": [139, 43, 3], "38": [14, 49, 177], "45": [6, 42, 156], "28": [203, 217, 68], "4": [152, 50, 10], "15": [232, 250, 254], "47": [93, 4, 0], "18": [234, 252, 255], "6": [93, 4, 0], "19": [14, 62, 198], "37": [14, 121, 139], "8": [104, 4, 2], "43": [11, 117, 130], "9": [104, 4, 2], "53": [144, 51, 10], "10": [204, 220, 85], "33": [234, 252, 255], "36": [233, 251, 255], "12": [236, 254, 255], "20": [7, 129, 152], "54": [149, 51, 12], "49": [99, 4, 0], "3": [94, 5, 0], "41": [138, 4, 1], "42": [9, 44, 160], "5": [126, 143, 39], "22": [8, 53, 182], "32": [24, 62, 195], "35": [188, 198, 49], "30": [235, 254, 248], "44": [11, 107, 123], "17": [188, 201, 69], "40": [12, 117, 136], "46": [94, 5, 0], "1": [140, 47, 6], "39": [12, 46, 170], "50": [171, 208, 250], "48": [139, 47, 10], "34": [206, 211, 65], "27": [6, 122, 137], "7": [152, 56, 16], "11": [235, 254, 250], "31": [207, 213, 65], "26": [7, 47, 169], "14": [10, 132, 145]}'

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