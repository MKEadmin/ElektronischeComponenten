import random
from machine import Pin
from utime import sleep
from CurrentTime import CurrentTime
import neopixel

PIN_DIN = 6
PIXELS_X = 16
PIXELS_Y = 16
PIXELS = PIXELS_X * PIXELS_Y

positions = []
for x in range(PIXELS):
    positions.append(x)

_np = neopixel.NeoPixel(Pin(PIN_DIN), PIXELS)
words = {"the"      : (15,14,13),
         "time"     : (11, 10, 9, 8),
         "is"       : (6,5),
         "minute"   : (112,113,114,115,116,117),
         "minutes"  : (112,113,114,115,116,117,118),
         "past"     : (120,121,122,123),
         "to"       : (123, 124),
         "a"        : (2,),
         "half"     : (3, 2, 1, 0),
         "quarter"  : (16, 17, 18, 19, 20,21,22),
         "clock"    : (176,177,178,179,180,181),
         "in"       : (183,184),
         "at"       : (185,186),
         "the_"     : (203,202,201),
         "night"    : (207,206,205,204,203),
         "morning"  : (199,198,197,196,195,194,193),
         "evening"  : (208,209,210,211,212,213,214),
         "afternoon": (215,216,217,218,219,220,221,222,223),
         "set"		: (226,225,224),
         #---------------------------------------
         "m20" 		: (23,24,25,26,27,28),
         "m19" 		: (71, 70,69,68,67,66,65,64),
         "m18" 		: (48,49,50,51,52,53,54,55),
         "m17" 		: (79,78,77,76,75,74,73,72,71),
         "m16" 		: (44,43,42,41,40,39,38),
         "m15" 		: (16, 17, 18, 19, 20,21,22),
         "m14" 		: (80,81,82,83,84,85,86,87),
         "m13" 		: (88,89,90,91,92,93,94,95),
         "m12" 		: (111,110,109,108,107, 106),
         "m11" 		: (106, 105,104,103,102,101),
         "m10" 		: (47,46,45),
         "m9" 		: (71, 70,69,68),
         "m8" 		: (48,49,50,51,52),
         "m7" 		: (79,78,77,76,75),
         "m6"  		: (44,43,42),
         "m5"  		: (56,57,58,59),
         "m4" 		: (80,81,82,83),
         "m3"  		: (100,99,98,97,96),
         "m2"  		: (37,36,35),
         "m1" 		: (35,34,33),
         #---------------------------------------
         "u0" 		: (154,155,156,157,158,159),
         "u12" 		: (154,155,156,157,158,159),
         "u11" 		: (139,138,137,136,135,134),
         "u10" 		: (163,162,161),
         "u9" 		: (134,133,132,131,),
         "u8" 		: (167,166,165,164,163),
         "u7" 		: (144,145,146,147,148),
         "u6" 		: (128,129,130),
         "u5" 		: (170,169,168,167),
         "u4" 		: (175,174,173,172),
         "u3" 		: (149,150,151,152,153),
         "u2" 		: (143,142,141),
         "u1" 		: (141,140,139),
         #---------------------------------------
         "00" 		: (240,),
         "10" 		: (241,),
         "20" 		: (242,),
         "30" 		: (243,),
         "40" 		: (244,),
         "50" 		: (245,),
         "0" 		: (246,),
         "1" 		: (247,),
         "2" 		: (248,),
         "3" 		: (249,),
         "4" 		: (250,),
         "5" 		: (251,),
         "6" 		: (252,),
         "7" 		: (253,),
         "8" 		: (254,),
         "9" 		: (255,)
         }


def clear():
    for x in positions:
        _np[x] = (0, 0, 0)
    _np.write()


def showPixel(p, color):
    _np[p] = color
    _np.write()

def showPixels(lst:tuple, color:tuple[int,int,int]):
    for x in lst:
        _np[x] = color
    _np.write()
    
def convertToSet(elements : list[list])->set:
    result = {item for sublist in elements for item in sublist}
    return result

def get_seconds(seconds:int)->list[list]:
    elements = []
    elements.append(words[f"{((seconds//10)*10):02}"])
    elements.append(words[f"{seconds%10}"])
    return elements
    
def get_elements(hour:int, minutes:int, seconds:int)->list[list]:
    elements = []
    elements.append(words[f"the"])
    elements.append(words[f"time"])
    elements.append(words[f"is"])
    elements.append(words[f"{((seconds//10)*10):02}"])
    elements.append(words[f"{seconds%10}"])
    if minutes == 0:
        elements.append(words[f"u{hour%12}"])
        elements.append(words[f"clock"])
    elif minutes == 30:
        elements.append(words[f"half"])
        elements.append(words[f"past"])
        elements.append(words[f"u{hour%12}"])
    elif minutes == 15:
        elements.append(words[f"a"])
        elements.append(words[f"quarter"])
        elements.append(words[f"past"])
        elements.append(words[f"u{hour%12}"]) 
    elif 0 < minutes <= 20:        
        elements.append(words[f"m{minutes}"])
        if minutes == 1:            
            elements.append(words[f"minute"])
        else:
            elements.append(words[f"minutes"])
        elements.append(words[f"past"])
        elements.append(words[f"u{hour%12}"])            
    elif minutes < 30:
        minutes = minutes-20
        elements.append(words[f"m20"]) 
        elements.append(words[f"m{minutes}"])
        elements.append(words[f"minutes"])
        elements.append(words[f"to"])        
        elements.append(words[f"u{hour%12}"])
    elif minutes == 45:
        hour += 1
        elements.append(words[f"a"])
        elements.append(words[f"quarter"])
        elements.append(words[f"to"])        
        elements.append(words[f"u{hour%12}"])
    elif 30 < minutes < 40:
        minutes = 40-minutes
        hour += 1
        elements.append(words[f"m20"]) 
        elements.append(words[f"m{minutes}"])        
        elements.append(words[f"minutes"])
        elements.append(words[f"to"])
        elements.append(words[f"u{hour%12}"])
    elif minutes >= 40:
        minutes = 60-minutes
        hour += 1
        elements.append(words[f"m{minutes}"])
        if minutes == 1:            
            elements.append(words[f"minute"])
        else:
            elements.append(words[f"minutes"])
        elements.append(words[f"to"])        
        elements.append(words[f"u{hour%12}"])  
        
    if 12 <= hour < 18:
        elements.append(words["in"])
        elements.append(words["the_"])
        elements.append(words["afternoon"])
    elif hour >= 18:
        elements.append(words["in"])
        elements.append(words["the_"])
        elements.append(words["evening"])
    elif 7 <= hour < 12:
        elements.append(words["in"])
        elements.append(words["the_"])
        elements.append(words["morning"])
    else:
        elements.append(words["at"])
        elements.append(words["night"])
        
    return elements

_oldPixels = set()
def show_time(hour:int, minutes:int, seconds:int):
    global _oldPixels
    print(f"{hour}:{minutes}:{seconds}")     
    pixels = get_elements(hour, minutes, seconds)
    
    newPixels = convertToSet(pixels)
    for pixel in _oldPixels - newPixels:
        showPixel(pixel, (0,0,0))
    
    for pixel in pixels:
        r = random.randint(50, 200)
        g = random.randint(50, 200)
        b = random.randint(50, 200)
        showPixels(pixel, (r,g,b))                    
    _oldPixels = newPixels

def showStatus(teller):
    global _oldPixels    
    pixels = get_seconds(teller%60)
    pixels.append(words["set"]) 
    newPixels = convertToSet(pixels)
    for pixel in _oldPixels - newPixels:
        showPixel(pixel, (0,0,0))
    
    for pixel in pixels:
        r = random.randint(50, 200)
        g = random.randint(50, 200)
        b = random.randint(50, 200)
        showPixels(pixel, (r,g,b))                    
    _oldPixels = newPixels
    
def main():
    clear()
    #currentTime = CurrentTime(0, False)
    currentTime = CurrentTime(1, True)
    while True:            
        hours, minutes, seconds = currentTime.getTime()
        show_time(hours, minutes, seconds )
        sleep(1)
            
if __name__ == "__main__":
    def test_time():
        clear()      
#         print("---- TEST THE FULL HOURS ----")
#         for hour in range(0, 24):
#             input(f"<Press enter> {hour}:0:0")            
#             show_time(hour, 0, 0)            
        print("---- TEST THE MINUTES ----")
        for minutes in range(0,60):
            input(f"<Press enter> 0:{minutes}:0")            
            show_time(0, minutes, 0)
            
    def test_keys():
        for key, value in words.items():
            clear()
            print(key)
            showPixels(value, (255,255,255))    
            sleep(1)
    def test_hours():
        for x in range(12, 0, -1):
            clear()
            print(x)
            showPixels(words[f"u{x}"], (255,0,255))
            sleep(1)
    def test_seconds():
        for x in range(0, 60):
            clear()
            print(x, f"{((x//10)*10):02}", f"{x%10}", )
            showPixels(words[f"{((x//10)*10):02}"], (255,0,255))
            showPixels(words[f"{x%10}"], (255,0,255))
            sleep(.5)
    main()
    #test_time()