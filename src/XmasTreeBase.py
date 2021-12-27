import time
import random
import neopixel2
import gc9a01

###################################################
class SmoothRainbow_LED:
    
    def __init__(self, ledCallBack, neoPixelStrip):
        print ("smooth Rainbow LED")
        self.hue = 0
        self.count = 0
        self.strip = neoPixelStrip
        self.ledCallBack = ledCallBack
        
    def run(self):
        self.hue += 2000
        color = self.strip.colorHSV(self.hue, 150, 30)
#        print(color)
        
        self.strip.fill(color)
        self.strip.show()
        self.count += 1
        if self.count > 7:
            self.hue = 0
            self.count = 0
            self.ledCallBack()

###################################################
class Rainbow_LED:
        
    def __init__(self, callBack, neoPixelStrip):
        print ("Rainbow LED")
        
        red = (255, 0, 0)
        orange = (255, 165, 0)
        yellow = (255, 150, 0)
        green = (0, 255, 0)
        blue = (0, 0, 255)
        indigo = (75, 0, 130)
        violet = (138, 43, 226)

        colors_rgb = (red, orange, yellow, green, blue, indigo, violet)
        # same colors as normaln rgb, just 0 added at the end
        colors_rgbw = [color+tuple([0]) for color in colors_rgb]
    
        self.brightnessSteps = [10, 30, 50, 100, 130, 150, 180, 200, 230]
        
        self.colors = colors_rgb

        self.callBack = callBack
        self.strip = neoPixelStrip
        self.count = 0
        
        self.index = 0

    def run(self):
        self.strip.brightness(random.randint(10, 150))
        self.strip.fill(self.colors[self.index])
        self.strip.show()
                
        self.index += 1
        if self.index >= len(self.colors): self.index=0
        
        self.count += 1
        if self.count > 7:
            self.count = 0
            self.callBack()
            

###################################################
class Angel_LED:
        
    def __init__(self, callBack, neoPixelStrip):
        print ("Angel LED")
        
        white = (200,200,200)
        orange = (255, 165, 0)
        yellow = (255, 150, 0)
        blue = (0, 0, 255)

        colors_rgb = (
            white,
            white,
            white
            )
        # same colors as normaln rgb, just 0 added at the end
 #       colors_rgbw = [color+tuple([0]) for color in colors_rgb]
    
        self.brightnessSteps = [200]
        
        self.colors = colors_rgb

        self.callBack = callBack
        self.strip = neoPixelStrip
        self.count = 0
        self.index = 0

    def run(self):
        self.strip.brightness(random.randint(200, 250))
        self.strip.fill(self.colors[self.index])
        self.strip.show()
                
        self.index += 1
        if self.index >= len(self.colors): self.index=0
        
        self.count += 1
        if self.count > 7:
            self.count = 0
            self.callBack()
            
            
######################################################           
class Firefly_LED:

    def __init__(self, ledCallBack, neoPixelStrip):
        
        print("Firefly")
        
        colors_rgb = [
            (232, 100, 255),  # Purple
            (200, 200, 20),  # Yellow
            (30, 200, 200),  # Blue
            (150,50,10),
            (50,200,10)
        ]


        self.ledCallBack = ledCallBack
        self.strip = neoPixelStrip
        self.count = 0
        
        # uncomment colors_rgbw if you have RGBW strip
        self.colors = colors_rgb
        # same colors as normaln rgb, just 0 added at the end
        #colors_rgbw = [color+tuple([0]) for color in colors_rgb]

        self.strip.brightness(10)

        self.max_len=20
        self.min_len = 5
        self.num_flashes = 10
        #pixelnum, posn in flash, flash_len, direction
        self.flashing = []

        for i in range(self.num_flashes):
            pix = random.randint(0, self.strip.num_leds - 1)
            col = random.randint(1, len(self.colors) - 1)
            flash_len = random.randint(self.min_len, self.max_len)
            self.flashing.append([pix, self.colors[col], flash_len, 10, 1])
#            print(pix)
#            print(col)
#            print (self.colors[col])
    
        self.strip.fill((0,0,0))
        self.strip.show()
#        print(self.flashing)

    def run(self):
        
        for i in range(self.num_flashes):
            pix = self.flashing[i][0]
            brightness = (self.flashing[i][3]/self.flashing[i][2])
#            print ("pix ", pix, " bright ", brightness)
            
            colr = (int(self.flashing[i][1][0]*brightness), 
                int(self.flashing[i][1][1]*brightness), 
                int(self.flashing[i][1][2]*brightness))
            
#            print ("Pix ", pix, " Colr ", colr)
            
            self.strip.set_pixel(pix, colr)

            if self.flashing[i][2] == self.flashing[i][3]:
                self.flashing[i][4] = -1
                
            if self.flashing[i][3] == 0 and self.flashing[i][4] == -1:
                pix = random.randint(0, self.strip.num_leds - 1)
                col = random.randint(0, len(self.colors) - 1)
                flash_len = random.randint(self.min_len, self.max_len)
                self.flashing[i] = [pix, self.colors[col], flash_len, 0, 1]
                
            self.flashing[i][3] = self.flashing[i][3] + self.flashing[i][4]
        
            self.strip.show()
            time.sleep(0.005)

  
        self.count += 1
        if self.count > 7:
            self.count = 0
            self.ledCallBack()
                
######################################################           
class ColorWave_LED:

    def __init__(self, ledCallBack, neoPixelStrip):
        print("ColorWave")
        self.ledCallBack = ledCallBack
        self.strip = neoPixelStrip
        self.count = 0
        
        self.red = (255, 0, 0)
        self.orange = (255, 50, 0)
        self.yellow = (255, 100, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.indigo = (100, 0, 90)
        self.violet = (200, 0, 100)

        self.colors_rgb = [
            self.red,
            self.orange,
            self.yellow,
            self.green,
            self.blue,
            self.indigo,
            self.violet
        ]
        
        # same colors as normaln rgb, just 0 added at the end
        self.colors_rgbw = [self.color+tuple([0]) for self.color in self.colors_rgb]

        self.colors = self.colors_rgb
        
        # uncomment colors_rgbw if you have RGBW strip
        # colors = colors_rgbw
        
        self.step = round(self.strip.num_leds / len(self.colors))
        self.strip.brightness(20)
        self.current_pixel = 0
        
        for self.color1, self.color2 in zip(self.colors, self.colors[1:]):
            
            self.strip.set_pixel_line_gradient(
                self.current_pixel,
                self.current_pixel + self.step,
                self.color1, self.color2)

            self.current_pixel += self.step

        self.strip.set_pixel_line_gradient(
            self.current_pixel,
            self.strip.num_leds - 1,
            self.violet, self.red)

    def run(self):

        self.strip.rotate_right(1)
        self.strip.show()
        
        self.count = self.count+1
        if self.count > 7:
            self.count = 0
            self.ledCallBack()
            
##################################################            

class Tree_LCD:
    

    def __init__(self, display):
        self.pics =  [
        "images/pslogo-240x240.jpg",
        "images/ds2-deathstranding-240x240.jpg",
        "images/ds1-spider-240x240-2.jpg",
        "images/ds3-yellow-240x240.jpg",
        "images/ds3-mario-240x240.jpg",
        "images/ds3-deathgame-240x240.jpg",
        "images/ps5logo-240x240.jpg" ]

        self.display = display
        self.index = 0
        self.lastTime = 0
        
    def run(self):
            if (time.ticks_ms() - self.lastTime) < 3000:
                return
            
            self.lastTime = time.ticks_ms()
            self.display.jpg(self.pics[self.index], 0, 0, gc9a01.SLOW)
            self.index += 1
            if self.index >= len(self.pics):
                self.index=0

#############################################################
class StarLED_Controller:
    
    def __init__(self, neoPixelStrip):
        
        self.ledModes = [
            Rainbow_LED(self.callBack, neoPixelStrip),
      #      SmoothRainbow_LED(self.callBack, neoPixelStrip),
            Firefly_LED(self.callBack, neoPixelStrip),
            ColorWave_LED(self.callBack, neoPixelStrip)
            ]
        
        self.currentMode = random.choice(self.ledModes)
        
    def run(self):
        self.currentMode.run()
        
    def callBack(self):
      #  print("callback")
        self.currentMode = random.choice(self.ledModes)
        
        
#############################################################
class Angel_Controller:
    
    def __init__(self, neoPixelStrip):
        self.currentMode = Angel_LED(self.callBack, neoPixelStrip)
        
    def run(self):
        self.currentMode.run()
        
    def callBack(self):
        pass
