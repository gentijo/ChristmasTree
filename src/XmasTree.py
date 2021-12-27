import gc
import time
import random
from machine import Pin, SPI
import gc9a01
from XmasTreeBase import *
from neopixel2 import Neopixel2

def XmasTree():
    gc.enable()
    print(gc.mem_alloc())
    print(gc.mem_free())


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
    print(gc.mem_alloc())
    print(gc.mem_free())

    runable = []

    runable.append(StarLED_Controller(Neopixel2(28,7)))
    runable.append(StarLED_Controller(Neopixel2(15,7)))
    runable.append(StarLED_Controller(Neopixel2(27,7)))
    runable.append(StarLED_Controller(Neopixel2(8,7)))
    runable.append(StarLED_Controller(Neopixel2(14,7)))
    runable.append(StarLED_Controller(Neopixel2(9,7)))
    runable.append(StarLED_Controller(Neopixel2(4,7)))
    runable.append(StarLED_Controller(Neopixel2(6,7)))
    runable.append(StarLED_Controller(Neopixel2(5,7)))
    runable.append(StarLED_Controller(Neopixel2(7,7)))
    runable.append(Tree_LCD(tft))
    runable.append(Angel_Controller(Neopixel2(22,1)))

    print (gc.mem_alloc())
    print (gc.mem_free())

    while True:
        gc.collect()

        for led in runable:
            led.run()
            time.sleep(0.1)
        
        temp = runable
        runable = []
        while len(temp) > 0:
            i = random.randint(0, len(temp)-1)
            runable.append(temp.pop(i))



        