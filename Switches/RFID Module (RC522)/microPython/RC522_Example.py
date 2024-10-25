from rc522 import RC522
import utime

reader = RC522(spi_id=0, sck=6, miso=4, mosi=7, cs=5, rst=3)
reader.init()

print("Bring TAG closer...")
print("")

while True:
    utime.sleep_ms(500)
    stat, tag_type = reader.request(reader.REQIDL)
    
    if stat != reader.OK:
        continue
        
    stat, uid = reader.SelectTagSN()
    if stat == reader.OK:
        card = int.from_bytes(bytes(uid), "little", False)
        print(f"CARD ID: {card}")
            
    