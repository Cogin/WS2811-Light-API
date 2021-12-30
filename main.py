import datetime
import board
import neopixel
import time
import random

pixels = neopixel.NeoPixel(board.D18, 50, brightness = 1)
while True:
    now = datetime.datetime.now() - datetime.timedelta(hours=6)
    timep = 1 - ((now.hour * 60 + now.minute) / 1440)
    print(round(timep*255),timep, now.hour, now.minute)
    pixels.fill((round(timep*255),round(timep*255),round(timep*200)))
    time.sleep(60)