import network
from animation import getNextChar
from secrets_AK import config
from utime import sleep

SLEEP = 5
station = network.WLAN(network.STA_IF)
station.active(False)
def connect(output = None):
    station.active(True)
    station.connect(config["WIFI"]["SSID"], config["WIFI"]["PASSWORD"])
    while station.isconnected() == False:
      print(getNextChar()+"\b", end="")
      sleep(SLEEP)
    
    if output != None:
        output(f"\nConnected with : {station.ifconfig()[0]}")
    return station

if __name__ == "__main__":
    def output(txt, theEnd="\n"):
        print(txt, end=theEnd)
    connect(output)
