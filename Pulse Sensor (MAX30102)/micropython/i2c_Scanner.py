import machine
i2c = machine.I2C(id=0, scl=machine.Pin(21), sda=machine.Pin(20))
devices = i2c.scan()

print('Scan i2c bus...')
if len(devices) == 0:
  print("No i2c device !")
else:
  print('i2c devices found:',len(devices))

  for device in devices:  
    print("Decimal address: ",device," | Hexa address: ",hex(device))
