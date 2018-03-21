import network
from mqtt import MQTTClient
import machine
import time

def settimeout(duration):
    pass

button_pin = machine.Pin(21, machine.Pin.IN)
button_state = 0

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(essid, password)

while not wlan.isconnected():
     machine.idle()

print("Connected to Wifi\n")
client = MQTTClient("publisher", broker_host, port=1883)
client.settimeout = settimeout
client.connect()

print("MQTT client connected")

time.sleep(1)

while True:
    new_button_state = button_pin.value()
    if new_button_state != button_state:
        button_state = new_button_state
        if button_state == 1:
            msg = 'ON'
        else:
            msg = 'OFF'
        client.publish('button', msg)

    machine.idle()
