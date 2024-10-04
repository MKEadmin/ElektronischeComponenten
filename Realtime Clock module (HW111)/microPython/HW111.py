import time
from machine import I2C

# Define the HW111 I2C address
HW111_I2C_ADDRESS = 0x68  # Common I2C address for HW111 RTC


class HW111:
    def __init__(self, i2c: I2C):
        self.i2c = i2c

    def _bcd_to_dec(self, bcd):
        """Convert BCD to decimal."""
        return (bcd // 16) * 10 + (bcd % 16)

    def _dec_to_bcd(self, dec):
        """Convert decimal to BCD."""
        return (dec // 10) << 4 | (dec % 10)

    def get_datetime(self):
        """Get the current date and time from the RTC."""
        self.i2c.writeto(HW111_I2C_ADDRESS, bytearray([0x00]))  # Set the pointer to the seconds register
        data = self.i2c.readfrom(HW111_I2C_ADDRESS, 7)  # Read 7 bytes

        seconds = self._bcd_to_dec(data[0] & 0x7F)  # Mask to prevent read of the oscillator stop bit
        minutes = self._bcd_to_dec(data[1])
        hour = self._bcd_to_dec(data[2] & 0x3F)  # Mask to prevent read of the 12/24 hour bit
        day = self._bcd_to_dec(data[3])
        month = self._bcd_to_dec(data[5])  # Month is stored in the 6th byte
        year = self._bcd_to_dec(data[6]) + 2000  # Year is stored in the 7th byte (assumed to be 2000-2099)

        return {
            'year': year,
            'month': month,
            'day': day,
            'hour': hour,
            'minute': minutes,
            'second': seconds
        }

    def set_datetime(self, year, month, day, hour, minute, second):
        """Set the date and time on the RTC."""
        if year < 2000 or year > 2099:
            raise ValueError("Year must be between 2000 and 2099.")

        data = bytearray(7)
        data[0] = self._dec_to_bcd(second)  # Seconds
        data[1] = self._dec_to_bcd(minute)  # Minutes
        data[2] = self._dec_to_bcd(hour)  # Hours
        data[3] = self._dec_to_bcd(day)  # Day
        data[4] = 0x00  # Weekday (not used)
        data[5] = self._dec_to_bcd(month)  # Month
        data[6] = self._dec_to_bcd(year - 2000)  # Year offset from 2000

        self.i2c.writeto(HW111_I2C_ADDRESS, bytearray([0x00]) + data)  # Write data starting at address 0x00
