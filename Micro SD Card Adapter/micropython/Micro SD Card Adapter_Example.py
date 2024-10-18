import machine
import uos
import sdcard

cs_pin = machine.Pin(17, machine.Pin.OUT)
spi = machine.SPI(0, baudrate=1000000, polarity=0, phase=0,bits=8, firstbit=machine.SPI.MSB,
                  sck=machine.Pin(18), mosi=machine.Pin(19), miso=machine.Pin(16))

sd = sdcard.SDCard(spi, cs_pin)

vfs = uos.VfsFat(sd)
uos.mount(vfs, "/sd")
fn = "/sd/sdtest.txt"

with open(fn, "w") as f:
    print("Writing data to file sdtest.txt...")
    f.write("This is a test for micro SD card\r\n")
    print("Writing to file completed")
    
with open(fn, "r") as f:
    print("Reading data from file sdtest.txt...")
    data = f.read()
    print("Data read completed")
    print("Data:",data)
