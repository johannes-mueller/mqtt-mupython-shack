import network
from mqtt import MQTTClient
import machine
import time

red_pin = machine.Pin(0, machine.Pin.OUT)
green_pin = machine.Pin(4, machine.Pin.OUT)

def mqtt_callback(topic, msg):
    print(topic, msg)
    tlist = topic.split(b'/')
    if tlist[0] != b'lights':
        return

    if tlist[1] == b'red':
        pin = red_pin
    else:
        pin = green_pin

    pin.value(msg == b'ON')

def settimeout(duration):
    pass



wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(essid, password)

while not wlan.isconnected():
     machine.idle()

print("Connected to Wifi\n")
client = MQTTClient("subscriber", broker_host, port=1883)
client.set_callback(mqtt_callback)
client.settimeout = settimeout
client.connect()

print("MQTT client connected")

time.sleep(1)

print("subscribing")
client.subscribe(b'lights/+')

while True:
    print("waiting for message")
    client.wait_msg()
