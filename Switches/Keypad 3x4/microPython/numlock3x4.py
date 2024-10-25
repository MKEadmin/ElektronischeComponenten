from machine import Pin
from utime import sleep


def _numinit(row1=3,row2=4,row3=5,row4=6,cols1=0,cols2=1,cols3=2 ):
    rows = [Pin(row1), Pin(row2), Pin(row3),Pin(row4)] 
    cols = [Pin(cols1), Pin(cols2), Pin(cols3)]  
    keypad = (('1', '2', '3'),
              ('4', '5', '6'),
              ('7', '8', '9'),
              ('*', '0', '#'))

    for row_pin in rows:
        row_pin.init(mode=Pin.IN, pull=Pin.PULL_UP)
    for col_pin in cols:
        col_pin.init(mode=Pin.OUT)
    return rows,cols,keypad


# Function to read the key pressed
def read_key():
    rows,cols,keypad = _numinit()
    for col_num, col_pin in enumerate(cols):
        col_pin.value(0)
        for row_num, row_pin in enumerate(rows):
            if row_pin.value() == 0:
                sleep(0.02)  # Debounce delay
                while row_pin.value() == 0:
                    pass  # Wait for key release
                col_pin.value(1)
                return keypad[row_num][col_num]
        col_pin.value(1)
    return None  # No key pressed
  
      
if __name__ == '__main__':
    while True:
        key = read_key()
        sleep(0.2)
        if key != None:
            print(key)





