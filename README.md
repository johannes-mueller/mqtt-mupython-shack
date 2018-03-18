# mqtt-mupython-shack
A simple mqtt demo using micropython for shackspace.

This demo aims at demonstrating how two esp32 chips can communicate with each
other via an mqtt broker.


## Prerequisites

This README assumes that you know how to handle esp32 dev boards and how to
install and handle micropython on them. In order to perform all the examples in
this demo you need two of those.

Additionally you need an mqtt broker (here we use mosquitto on an ubuntu machine as an
example) as well as some mqtt cli-client. These can be installed easily on
ubuntu by
```
sudo apt install mosquitto mosquitto-clients
```

Furthermore does not explain how to handle 3rd party software and hardware. It
is assumed that average hackers can figure out on their own which software to
use, where to get it and how to handle it. Similarly we don't explain how to
set up simple circuits using an esp32 dev board.

In order for the esp32s to communicate via the mqtt broker, both need wlan
access to a wlan network by which they can access the mqtt broker. So you need
to make sure that the mqtt broker is listening on an interface accessible from
your network.

## Installation

First copy `mqtt.py` on both esp32. Then for every demo you need to adjust the
concerning `main-*.py` file in the following way:


* adjust the credidentials `essid` and `password` so that they match your wlan.

* adjust the `broker_ip` to match to the ip address of your broker.


Then copy the `main-*.py` file to the esp32(s) as `/main.py`. If you want to
observe what the esp32s are doing you can connect to their serial
interfaces. To observe what is going on at the mqtt broker `tail -f` to the
logfile. Maybe you need to adjust the loglevel in the configuration.

Usually you need to press the reset button on the dev boards in order to launch
the demo properly.


## Demos

### Subscribing to messages

We put two LEDs (red and green) to the GPIO pins of the esp32. By subscribing
to the mqtt topic `/light/*` we can receive message to switch the corresponding
LED on and off.

Copy `main-subscribe.py` to the esp32 as `/main.py` and press the reset button.

Now if on the mqtt bus the message topic `/light/green` and payload `on` is
published the green LED should light up. If you have installed the
`mosquitto-clients` you can do that by
```
mosquitto_pub -h localhost -t "/light/green" -m "on"
```

By giving the message the payload `off` the LED switches off again. Same for
the red LED for the topic `/light/red`


### Publishing messages

Now we connect a switch to an GPIO pin and when the switch changes position we
publish a message which another mqtt client can subscribe to.


### Publishing and receiving messages on the same esp32

This is a bit trickier.
