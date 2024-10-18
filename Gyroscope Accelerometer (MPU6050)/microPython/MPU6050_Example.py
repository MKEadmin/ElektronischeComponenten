from machine import Pin, I2C
import time
import math

# MPU6050 default address
MPU6050_ADDR = 0x68

# MPU6050 Registers
MPU6050_ACCEL_XOUT_H = 0x3B
MPU6050_PWR_MGMT_1 = 0x6B
MPU6050_GYRO_XOUT_H = 0x43

# Initialize I2C
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)

# MPU6050 setup function
def mpu6050_init():
    # Wake up the MPU6050
    i2c.writeto_mem(MPU6050_ADDR, MPU6050_PWR_MGMT_1, b'\x00')

# Read raw data from registers
def read_raw_data(register):
    high = i2c.readfrom_mem(MPU6050_ADDR, register, 1)[0]
    low = i2c.readfrom_mem(MPU6050_ADDR, register+1, 1)[0]
    value = (high << 8) | low
    if value > 32768:
        value = value - 65536
    return value

# Read accelerometer data
def read_accel_data():
    accel_x = read_raw_data(MPU6050_ACCEL_XOUT_H)
    accel_y = read_raw_data(MPU6050_ACCEL_XOUT_H + 2)
    accel_z = read_raw_data(MPU6050_ACCEL_XOUT_H + 4)
    return accel_x, accel_y, accel_z

# Read gyroscope data
def read_gyro_data():
    gyro_x = read_raw_data(MPU6050_GYRO_XOUT_H)
    gyro_y = read_raw_data(MPU6050_GYRO_XOUT_H + 2)
    gyro_z = read_raw_data(MPU6050_GYRO_XOUT_H + 4)
    return gyro_x, gyro_y, gyro_z

# Main function to print sensor values
def main():
    mpu6050_init()
    while True:
        accel_x, accel_y, accel_z = read_accel_data()
        gyro_x, gyro_y, gyro_z = read_gyro_data()

        # Convert raw data to actual values (acceleration in g, gyro in degrees/sec)
        accel_x /= 16384.0
        accel_y /= 16384.0
        accel_z /= 16384.0
        gyro_x /= 131.0
        gyro_y /= 131.0
        gyro_z /= 131.0

        print("Accel (g) - X: {:.2f}, Y: {:.2f}, Z: {:.2f}".format(accel_x, accel_y, accel_z))
        print("Gyro (deg/s) - X: {:.2f}, Y: {:.2f}, Z: {:.2f}".format(gyro_x, gyro_y, gyro_z))
        print()
        
        time.sleep(1)

# Run the main loop
main()
