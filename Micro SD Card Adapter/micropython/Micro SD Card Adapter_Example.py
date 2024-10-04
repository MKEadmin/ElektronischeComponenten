import machine
import os
import sdcard
import time

# Setup SPI interface (using SPI0)
spi = machine.SPI(0, baudrate=1000000, sck=machine.Pin(18), mosi=machine.Pin(19), miso=machine.Pin(16))

# Chip Select (CS) pin
cs = machine.Pin(17, machine.Pin.OUT)

# Initialize SD card
try:
    sd = sdcard.SDCard(spi, cs)  # Try initializing the SD card
    print("SD Card initialized successfully.")
except Exception as e:
    print("Failed to initialize SD card:", e)
    raise

# Mount the filesystem
try:
    vfs = os.VfsFat(sd)
    os.mount(vfs, "/sd")
    print("Filesystem mounted successfully.")
except Exception as e:
    print("Failed to mount filesystem:", e)
    raise

# List files in the root directory
print("Files on SD card:", os.listdir("/sd"))

# Create a file and write data
try:
    with open("/sd/hello.txt", "w") as file:
        file.write("Hello, MicroSD card from Raspberry Pi Pico!")
        print("Data written to hello.txt successfully.")
except Exception as e:
    print("Failed to write to SD card:", e)

# Read the content of the file
try:
    with open("/sd/hello.txt", "r") as file:
        content = file.read()
        print("File content:", content)
except Exception as e:
    print("Failed to read from SD card:", e)

# Unmount the filesystem
try:
    os.umount("/sd")
    print("SD card unmounted successfully.")
except Exception as e:
    print("Failed to unmount SD card:", e)
