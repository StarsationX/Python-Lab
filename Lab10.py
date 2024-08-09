from machine import Pin
from utime import sleep

print("Phiranat Termprayoon 11. | Starsation")

led = [15, 18, 22, 23]

for i in range(4):
        led[i] = Pin(led[i], Pin.OUT)

def fd():
    #Front -> Back
    for i in range(4):
        led[i].on()
        sleep(.5)
        led[i].off()
        sleep(.5)

def bk():
    # Back -> Front
    for i in reversed(led):
        i.on()
        sleep(.5)
        i.off()
        sleep(.5)

def mo():
    # Mid -> Out
    led[0].off()
    led[3].off()
    led[1].on()
    led[2].on()
    sleep(.5)
    led[1].off()
    led[2].off()
    led[0].on()
    led[3].on()
    sleep(.5)

def mi():
    # Out -> Mid
    led[1].off()
    led[2].off()
    led[0].on()
    led[3].on()
    sleep(.5)
    led[0].off()
    led[3].off()
    led[1].on()
    led[2].on()
    sleep(.5)

while True:
    fd()
    bk()
    mo()
    mi()