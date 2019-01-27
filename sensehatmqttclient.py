#!/usr/bin/python3

from sense_hat import SenseHat,  ACTION_RELEASED
from time import sleep
from random import randint
import datetime

import paho.mqtt.client as mqtt

r = (153,0,0)
b = (0,0,153)
g = (0,153,0)
w = (153,153,153)
y = (153,153,0)
o = (153,76,0)
v = (76,0,153)
n = (0,0,0)
t = (0,153,153)

pixels_sun = [
            y,b,b,b,b,b,b,y,
            b,y,b,b,b,b,y,b,
            b,b,b,y,y,b,b,b,
            b,b,y,o,o,y,b,b,
            b,b,y,o,o,y,b,b,
            b,b,b,y,y,b,b,b,
            b,y,b,b,b,b,y,b,
            y,b,b,b,b,b,b,y
        ]

pixels_cloud = [
            b,b,b,b,b,b,b,b,
            b,b,w,b,w,b,b,b,
            b,w,w,w,w,w,b,b,
            w,w,w,w,w,w,w,b,
            b,w,w,w,w,w,b,b,
            b,b,w,b,w,b,b,b,
            b,b,b,b,b,b,b,b,
            b,b,b,b,b,b,b,b
            ]

pixels_rain = [
            n,n,n,n,n,n,n,n,
            n,n,w,n,w,n,n,n,
            n,w,w,w,w,w,n,n,
            w,w,w,w,w,w,w,n,
            n,w,w,w,w,w,n,n,
            n,t,w,t,w,t,n,n,
            t,n,t,n,t,n,n,n,
            n,t,n,t,n,n,n,n
            ]


THE_BROKER = "localhost"
CLIENT_ID = ""


def on_connect(client, userdata, flags, rc):
    print("Connected to ", client._host, "port: ", client._port)
    print("Flags: ", flags, "returned code: ", rc)

    client.subscribe("peek/temperature", qos=0)
    client.subscribe("peek/pressure", qos=0)
    client.subscribe("peek/humidity", qos=0)
    client.subscribe("show/sun", qos=0)
    client.subscribe("show/cloud", qos=0)
    client.subscribe("show/rain", qos=0)
    client.subscribe("show/message", qos=0)


def on_message(client, userdata, msg):
    print("DEBUG: msg received with topic: {} and payload: {}".format(msg.topic, str(msg.payload)))
    if (msg.topic == "peek/temperature"):
        client.publish("sensehat/temperature", 
                   payload="Temperature: "+str(round(sense.get_temperature(),2))+" C", 
                   qos=0, 
                   retain=False)
    elif (msg.topic == "peek/pressure"):
        client.publish("sensehat/pressure", 
                   payload="Pressure: "+str(round(sense.get_pressure(),2))+" Millibars", 
                   qos=0, 
                   retain=False)
    elif (msg.topic == "peek/humidity"):
        client.publish("sensehat/humidity", 
                   payload="Humidity: "+str(round(sense.get_humidity(),2))+" %", 
                   qos=0, 
                   retain=False)
    elif (msg.topic == "show/sun"):
        sense.clear()
        sense.set_pixels(pixels_sun)
        sleep(2)
        sense.clear()
    elif (msg.topic == "show/cloud"):
        sense.clear()
        sense.set_pixels(pixels_cloud)
        sleep(2)
        sense.clear()
    elif (msg.topic == "show/rain"):
        sense.clear()
        sense.set_pixels(pixels_rain)
        sleep(2)
        sense.clear()
    elif (msg.topic == "show/message"):
        sense.clear()
        sense.show_message(str(msg.payload))
        sleep(2)
        sense.clear()
    else:
        sense.show_message("???")


sense = SenseHat()


client = mqtt.Client(client_id=CLIENT_ID, 
                     clean_session=True, 
                     userdata=None, 
                     protocol=mqtt.MQTTv311, 
                     transport="tcp")

client.on_connect = on_connect
client.on_message = on_message

client.connect(THE_BROKER, port=1883, keepalive=60)

client.loop_start()
while(1):
    client.publish("sensehat/temperature", 
                   payload="Temperature: "+str(round(sense.get_temperature(),2))+" C", 
                   qos=0, 
                   retain=False)
    sleep(5)
client.loop_stop()



