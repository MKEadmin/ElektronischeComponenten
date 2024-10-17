from machine import Pin

led = Pin(25, Pin.OUT)


def blinkLed():
    for _ in range(10):
        led.on()
        sleep(0.1)
        led.off()
        sleep(0.1)


def ledOn():
    led.on()


def ledOff():
    led.off()
