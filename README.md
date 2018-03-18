# mqtt-mupython-shack
A simple mqtt demo using micropython for shackspace.

This demo aims at demonstrating how two esp32 chips can communicate with each
other via an mqtt broker. This is not meant to be used for anything except to
learn how mqtt works. We are using it in our local hackspace to play around
with mqtt on esp32. When I say learning I mean that I am myself learning. So
there might be lots of errors or stupidities in there. Feel free to pull
request :)


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

First copy `mqtt.py` on both esp32. Then adjust `boot.py`

* add the credidentials `essid` and `password` so that they match your wlan.

* the `broker_ip` to match to the ip address of your broker.

and put `boot.py` to the esp32.


Then copy the `main-*.py` file to the esp32(s) as `/main.py`. If you want to
observe what the esp32s are doing you can connect to their serial
interfaces. To observe what is going on at the mqtt broker `tail -f` to the
logfile. Maybe you need to adjust the loglevel in the configuration.

Usually you need to press the reset button on the dev boards in order to launch
the demo properly.

## Credits

The file `mqtt.py` is a modified version from the `umqtt` simple client of
`micropython-lib` that can be found on Github.


## Demos

### Subscribing to messages

We put two LEDs (red and green) to the GPIO pins of the esp32. By subscribing
to the mqtt topic `/light/*` we can receive message to switch the corresponding
LED on and off.

Copy the adjusted `main-subscribe.py` to the esp32 as `/main.py` and press the reset button.

Now if on the mqtt bus the message topic `/light/green` and payload `on` is
published the green LED should light up. If you have installed the
`mosquitto-clients` you can do that by
```
mosquitto_pub -h localhost -t "light/green" -m "on"
```

By giving the message the payload `off` the LED switches off again. Same for
the red LED for the topic `/light/red`


### Publishing messages

Now we connect a button to an GPIO pin and when the button changes state we
publish a message which another mqtt client can subscribe to.

Copy the adjusted `main-publish.py` to the esp32 as `/main.py`

By subscribing to the topic `/button` a mqtt client can receive messages when the
button is pressed or released.
```
mosquitto_sub -h localhost -t "button"
```

### Hack it

Now you can play around with this. For example you can adjust the message that
`main-publish.py` publishes or `main-subscribe.py` subscribes to in order to
use the button at one esp32 to switch the LEDs at another.

Have fun.


### Publishing and receiving messages on the same esp32

This is a bit trickier.


## TODO

* Better idling?

* Authentication

* Encryption
