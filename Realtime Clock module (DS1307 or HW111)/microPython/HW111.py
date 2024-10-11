from machine import I2C
from micropython import const

DATETIME_REG = const(0)  # 0x00-0x06 for time/date registers
CHIP_HALT = const(128)
CONTROL_REG = const(7)  # 0x07 for control register


class HW111:
    """Driver for the HW111 RTC (similar to DS1307)."""

    def __init__(self, i2c, addr=0x68):
        self.i2c = i2c
        self.addr = addr
        self.weekday_start = 1  # If weekday is needed
        self._halt = False

    def _dec2bcd(self, value):
        """Convert decimal to binary-coded decimal (BCD)."""
        return (value // 10) << 4 | (value % 10)

    def _bcd2dec(self, value):
        """Convert BCD format to decimal."""
        return ((value >> 4) * 10) + (value & 0x0F)

    def datetime(self, datetime=None):
        """Get or set the date and time."""
        if datetime is None:
            # Read current datetime from RTC
            buf = self.i2c.readfrom_mem(self.addr, DATETIME_REG, 7)
            return (
                self._bcd2dec(buf[6]) + 2000,  # year
                self._bcd2dec(buf[5]),  # month
                self._bcd2dec(buf[4]),  # day
                self._bcd2dec(buf[3] - self.weekday_start),  # weekday (optional)
                self._bcd2dec(buf[2]),  # hour
                self._bcd2dec(buf[1]),  # minute
                self._bcd2dec(buf[0] & 0x7F),  # second
                0  # subseconds (not used)
            )
        # Set datetime on RTC
        buf = bytearray(7)
        buf[0] = self._dec2bcd(datetime[6]) & 0x7F  # seconds
        buf[1] = self._dec2bcd(datetime[5])  # minutes
        buf[2] = self._dec2bcd(datetime[4])  # hours
        buf[3] = self._dec2bcd(datetime[3] + self.weekday_start)  # weekday (optional)
        buf[4] = self._dec2bcd(datetime[2])  # day
        buf[5] = self._dec2bcd(datetime[1])  # month
        buf[6] = self._dec2bcd(datetime[0] - 2000)  # year

        if self._halt:
            buf[0] |= CHIP_HALT  # Stop clock if halted

        # Write the datetime to RTC
        self.i2c.writeto_mem(self.addr, DATETIME_REG, buf)

    def halt(self, val=None):
        """Halt or resume the clock."""
        if val is None:
            return self._halt
        reg = self.i2c.readfrom_mem(self.addr, DATETIME_REG, 1)[0]
        if val:
            reg |= CHIP_HALT
        else:
            reg &= ~CHIP_HALT
        self._halt = bool(val)
        self.i2c.writeto_mem(self.addr, DATETIME_REG, bytearray([reg]))

    def square_wave(self, sqw=0, out=0):
        """Control the square wave output on the SQ pin."""
        rs0 = 1 if sqw in [4, 32] else 0
        rs1 = 1 if sqw in [8, 32] else 0
        out = 1 if out > 0 else 0
        sqw = 1 if sqw > 0 else 0
        reg = rs0 | (rs1 << 1) | (sqw << 4) | (out << 7)
        self.i2c.writeto_mem(self.addr, CONTROL_REG, bytearray([reg]))

