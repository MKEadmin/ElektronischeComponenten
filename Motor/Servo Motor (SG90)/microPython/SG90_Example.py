from machine import Pin, PWM
from time import sleep


servo = PWM(Pin(16))
servo.freq(50)  

def set_angle(angle):
    min_duty = 2000   
    max_duty = 8000   
    duty = int(min_duty + (angle / 180) * (max_duty - min_duty))
    servo.duty_u16(duty)

while True:
    # Sweep from 0° to 180°
    for angle in range(0, 181, 5):
        set_angle(angle)
        sleep(0.02)  # 20 ms delay
    
    # Sweep from 180° to 0°
    for angle in range(180, -1, -5):
        set_angle(angle)
        sleep(0.02)  # 20 ms delay

