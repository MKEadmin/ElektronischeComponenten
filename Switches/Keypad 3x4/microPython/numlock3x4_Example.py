from numlock3x4 import read_key #Libary for the numlock
from utime import sleep

user_Code = []
while True: 
    key = read_key()	#reads numpad inputs
    print(key)
    sleep(.1)
