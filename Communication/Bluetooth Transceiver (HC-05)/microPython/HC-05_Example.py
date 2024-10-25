from machine import UART
from machine import Pin
from utime import sleep

#roep uart aan
uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

#als er iets binnen komt op je bluetooth device, return the value. anders value = None
#leest alle inputs die het device binnen krijgt, als je sleep(5) in je code hebt,
#leest die nogsteeds alles op wat gestuurd is, maar met een delay van 5 op je shell
def listenToUart():
    if uart.any():
        data = uart.readline()
        return data.decode('utf-8').strip()

#stuurt string naar bluetooth device
def sendToUart(text):
    uart.write(text)

"""
Om de bluetooth verbinding te testen:
1 Download op een Android telefoon de app "Serial Bluetooth Terminal".
2 zoek naar bluetooth connecties op je telefoon. 
3 verbind met HC-0X
4 vul pincode in, standaard pincode is 0000 of 1234. je kan er nog niet mee koppelen.
5 open de erial Bluetooth Terminal app
6 klik op de menu bar links boven
7 selecteer devices
8 selecteer vervolgens Bluetooth Classic
9 selecteer jou device
10 ga terug naar terminal, als het goed is staat er nu Connecting to HC-0X ... -> Connected
11 run deze code, in je shell zie je None. in de app kan je een text sturen. deze zie je vervolgens ook in je shell
Goed gedaan!
"""

if __name__ == "__main__":
    while True:
        print(listenToUart())
        sendToUart("test\n")
        sleep(1)
        
        

        
