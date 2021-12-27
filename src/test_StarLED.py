# Example showing use of HSV colors
import time
from neopixel import Neopixel

numpix = 7
strip = Neopixel(numpix, 0, 28, "GRB")

hue = 0
while(True):
    color = strip.colorHSV(hue, 150, 30)
    print(color)
    strip.fill(color)
    strip.show()
    
    hue += 150
    