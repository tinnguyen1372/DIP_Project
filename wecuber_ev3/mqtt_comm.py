#MQTT communication
import paho.mqtt.client as mqtt
import logging
# logging.basicConfig(filename='rubiks.log',
logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)12s %(levelname)8s: %(message)s')
log = logging.getLogger(__name__)

# Color the errors and warnings in red
logging.addLevelName(logging.ERROR, "\033[91m   %s\033[0m" % logging.getLevelName(logging.ERROR))
logging.addLevelName(logging.WARNING, "\033[91m %s\033[0m" % logging.getLevelName(logging.WARNING))

client = mqtt.Client()
message = ''
def on_connect(client, userdata, flags, rc):
    client.subscribe("topic/pc_to_ev3")

def on_message(client, userdata, msg):
    global message
    message = str(msg.payload.decode('utf-8'))
    log.info('Received Solution from PC: {}'.format(message))
    client.disconnect()

def send_to_pc(scanresult):
    
    client.connect("localhost",1883,60)
    client.publish("topic/ev3_to_pc", scanresult)
    log.info("Scan result published to PC")

    client.on_connect = on_connect
    client.on_message = on_message

    client.loop_forever()
    return message
    
