import network, urequests, utime, ntptime
from machine import Timer
import machine
from secrets_AK import config
import localNetwork

def output(txt, theEnd="\n"):
    print(txt, end=theEnd)
        
station = localNetwork.connect(output)

MINUTE = 60000
TIMER_DELAY_CLOCK    = 30 # MINUTE to get the latest time
HTTP_OK = 200

timer_clock    = Timer(-1)
_showStatus = None
def init(showStatus):
    global _showStatus
    _showStatus = showStatus
    query_time   (None)
    timer_clock  .init(period=TIMER_DELAY_CLOCK   * MINUTE, mode=Timer.PERIODIC, callback=query_time)    
    

# decorator for checking WiFi status
def station_check_decorator(func):
    def wrapper(*args, **kwargs):
        if not station.isconnected():
            # stop timers
            timer_clock.deinit()
            # reboot
            reset()
        else:
            # run decorated functions
            func(*args, **kwargs)
    return wrapper

# query time from NTP server
@station_check_decorator
def query_time(timer) -> None:
    print("Update Time")
    teller = 0
    while True:
        try:
            print(".", end="")
            ntptime.settime()
            print(f"Local time : {machine.RTC().datetime()}")
            break
        except Exception as e:
            print("Failed to sync time via NTP.")
            print("Error details:", e)
            _showStatus(teller)
            teller += 1
            utime.sleep(1)
