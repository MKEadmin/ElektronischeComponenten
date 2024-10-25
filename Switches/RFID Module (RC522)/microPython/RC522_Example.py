from rc522 import RC522
import utime

reader = RC522(spi_id=0, sck=6, miso=4, mosi=7, cs=5, rst=22)

print("Bring TAG closer...")
print("")

while True:
    reader.init()
    (stat, tag_type) = reader.request(reader.REQIDL)
    if stat == reader.OK:
        (stat, uid) = reader.SelectTagSN()
        if stat == reader.OK:
            card = int.from_bytes(bytes(uid), "little", False)
            print("CARD ID: " + str(card))
utime.sleep_ms(500)