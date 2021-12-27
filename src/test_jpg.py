'''
jpg.py

    Draw a full screen jpg using the slower but less memory intensive method
    of blitting each Minimum Coded Unit (MCU) block. Usually 8×8 pixels but can
    be other multiples of 8.

    GC9A01 display connected to a Raspberry Pi Pico.

    Pico Pin   Display
    =========  =======
    14 (GP10)  BL
    15 (GP11)  RST
    16 (GP12)  DC
    17 (GP13)  CS
    18 (GND)   GND
    19 (GP14)  CLK
    20 (GP15)  DIN

    bigbuckbunny.jpg (c) copyright 2008, Blender Foundation / www.bigbuckbunny.org
'''

import gc
import time 
from machine import Pin, SPI
import gc9a01

gc.enable()
gc.collect()


def main():
    '''
    Decode and draw jpg on display
    '''
    spi = SPI(0, baudrate=80000000, sck=Pin(18), mosi=Pin(19))
    tft = gc9a01.GC9A01(
        spi,
        240,
        240,
        reset=Pin(26, Pin.OUT),
        cs=Pin(17, Pin.OUT),
        dc=Pin(21, Pin.OUT),
        backlight=Pin(20, Pin.OUT),
        rotation=2)

    # enable display and clear screen
    tft.init()

    # cycle thru jpg's
    while True:
        for image in [
            "images/pslogo-240x240.jpg",
            "images/ds2-deathstranding-240x240.jpg",
            "images/ds1-spider-240x240-2.jpg",
            "images/ds3-yellow-240x240.jpg",
            "images/ds3-mario-240x240.jpg",
            "images/ds3-deathgame-240x240.jpg",
            "images/ps5logo-240x240.jpg" ]:
            tft.jpg(image, 0, 0, gc9a01.FAST)
            time.sleep(1)


main()
