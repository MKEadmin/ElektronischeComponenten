"""
MicroPython max7219 cascadable 8x8 LED matrix driver

Licensed under MIT, found in LICENSE.txt
    Copyright (c) 2017 Mike Causer
    Copyright (c) 2022 Leo Spratt
"""
from micropython import const
from framebuf import FrameBuffer, MONO_HLSB

_NOOP = const(0)
_DIGIT0 = const(1)
_DECODEMODE = const(9)
_INTENSITY = const(10)
_SCANLIMIT = const(11)
_SHUTDOWN = const(12)
_DISPLAYTEST = const(15)


class Matrix8x8(FrameBuffer):
    def __init__(self, spi, cs, num, format=MONO_HLSB):
        """
        Driver for cascading MAX7219 8x8 LED matrices.

        >>> from machine import Pin, SPI
        >>> from max7219 import Matrix8x8
        >>> spi = SPI(1)
        >>> display = Matrix8x8(spi, Pin('X5'), 4)
        >>> display.text('1234')
        >>> display.show()

        """
        self._spi = spi
        self._cs = cs
        self._cs.init(self._cs.OUT, True)
        self._num = num
        self._buffer = bytearray(8 * self._num)

        super().__init__(self._buffer, 8 * self._num, 8, format)

        self._write_init()

    def _write(self, command, data):
        self._cs(0)
        for _ in range(self._num):
            self._spi.write(bytearray([command, data]))
        self._cs(1)

    def _write_init(self):
        for command, data in (
            (_SHUTDOWN, 0),
            (_DISPLAYTEST, 0),
            (_SCANLIMIT, 7),
            (_DECODEMODE, 0),
            (_SHUTDOWN, 1),
        ):
            self._write(command, data)

    def brightness(self, value):
        if not 0 <= value <= 15:
            raise ValueError("Brightness out of range")
        self._write(_INTENSITY, value)

    def text(self, s, x=0, y=0, c=1):
        super().text(s, x, y, c)

    def text_from_glyph(self, s, glyphs, x_offset=0, y_offset=0):
        col = 0
        for char in s:
            glyph = glyphs.get(char)

            if glyph:
                for y in range(8):
                    for x in range(8):
                        self.pixel(x+col+x_offset, y+y_offset, glyph[y][x])
            else:
                self.text(char, col+x_offset, y_offset)

            col += 8

    def show(self):
        for y in range(8):
            self._cs(0)
            for m in range(self._num):
                self._spi.write(bytearray([_DIGIT0 + y, self._buffer[(y * self._num) + m]]))
            self._cs(1)

    def zero(self):
        self.fill(0)

    def shutdown(self):
        self._write(_SHUTDOWN, 0)

    def wake(self):
        self._write(_SHUTDOWN, 1)

    def test(self, enable=True):
        self._write(_DISPLAYTEST, int(enable))
