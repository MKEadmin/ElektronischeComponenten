import time
from machine import I2C, Pin

class ADC:
    def __init__(self, i2c, address):
        self.i2c = i2c
        self.address = address

    A0 = 0
    A1 = 1
    A2 = 2
    A3 = 3

    def readConfig(self):
        self.i2c.writeto(self.address, bytearray([1]))
        result = self.i2c.readfrom(self.address, 2)
        
        return result[0] << 8 | result[0]

    def readValue(self,channel):
        config = self.readConfig()
        
        config &= ~(7<<12)
        config &= ~(7<<9)
        
        config |= (7 & (4 + channel))<<12
        config |= (1<<15)
        config |= (1<<9)
        
        config =[int(config>>i & 0xff) for i in [8,0]]
        self.i2c.writeto(self.address, bytearray([1] + config))
        config = self.readConfig()
        while (config & 0x8000) == 8:
            config = self.readConfig()
            
        self.i2c.writeto(self.address, bytearray([0]))
        result = self.i2c.readfrom(self.address, 2)
        
        return result[0]<<8 | result[0]

    def readVolts(self,channel):
        value = self.readValue(channel)
        return str(((4.096 * 2) / 0xffff) * value)[0:4]


