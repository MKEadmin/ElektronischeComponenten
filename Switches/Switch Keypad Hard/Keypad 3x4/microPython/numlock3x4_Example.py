from numlock_3x4 import read_key		#Libary for the numlock

user_Code = []
while True: 
    key = read_key()	#reads numpad inputs
    if key != None:
        user_Code.append(key)
        if key == "#":
            print(user_Code)
            user_Code = []