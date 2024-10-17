from machine import Pin
from utime import sleep
import utime

class IRQButton():
    """
        pull is Pin.PULL_UP or Pin.PULL_DOWN
    """
    def __init__(self, pin, callbackPressed = None, data = None, pull = Pin.PULL_UP, notifyAllChanges = False, debug = False):
        self._pin = Pin(pin, Pin.IN, pull)
        self._debounce_time = 0
        self._callbackPressed = callbackPressed
        self._pull = pull
        self._notifyAllChanges = notifyAllChanges
        self._data = data # data returned with callback
        self._debug = debug
        if callbackPressed != None:
            #Pin.IRQ_RISING| Pin.IRQ_FALLING
            self._pin.irq(trigger=Pin.IRQ_FALLING, handler=self._handler)
    
    def value(self):
        return self._pin.value()
    
    _lastValue = None
    def _handler(self, pin):
        #print(f"_handler({pin})")
        newValue = self.value()
        elapsedTime = utime.ticks_ms()-self._debounce_time
        if self._lastValue == newValue:
            return
        if elapsedTime < 300:
            return
        self._lastValue = newValue
        if not self._notifyAllChanges:
            if self._pull == Pin.PULL_UP and newValue == 1:
                return
            if self._pull == Pin.PULL_DOWN and newValue == 0:
                return
        if self._debug:
            print("_handler", pin, elapsedTime, "last", self._lastValue, "new", newValue)
        self._debounce_time=utime.ticks_ms()
        
        self._pin.irq(handler=None)
        if self._data == None:
            self._callbackPressed()
        else:
            self._callbackPressed(self._data)
        sleep(0.3)
        if self._debug:
            print("Pressed", self._pinPressed.value())
        self._pin.irq(handler=self._handler)
    
if __name__ == "__main__":
    counter = 0
    def pressed(data):
        global counter
        print(f"{counter:5} Pressed({data})")
        counter += 1
    btn = IRQButton(26, pressed, "A", notifyAllChanges = True)
    btn = IRQButton(27, pressed, "B", notifyAllChanges = True)
    
    while True:
        machine.idle() # Delay to prevent excessive CPU usage






