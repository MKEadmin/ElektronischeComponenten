from machine import UART
import math
from utime import sleep
import random

uart = UART(0, 9600)


def write(data1, data2):
    line = f'{data1}:{data2}'
    print("Writing data to phone : ", line)
    uart.write(line)


if __name__ == "__main__":
    import math

    HOOGTE = 1  # meter
    STEPS = 20
    NUMBER_OF_SIN = 10
    STEP = math.pi / STEPS
    while True:
        i = 0
        while i < NUMBER_OF_SIN * STEPS:
            hoogte1 = (HOOGTE / 2) * (1 + math.sin(i * STEP))
            hoogte2 = (HOOGTE / 2) * (1 + math.sin(i * STEP + math.pi))
            print(round(hoogte1, 3), round(hoogte2, 3), round(hoogte1 + hoogte2, 3))
            i += 1
            write(hoogte1, hoogte2)
            sleep(1)
