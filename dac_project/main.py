# This is your main script.

import math 
from machine import Pin, DAC, Timer 

#sine = bytearray(2)

#for i in range(len(sine)):
#    sine[i] = 128 + int(127 * math.sin(2 * math.pi * i / len(sine)))


"""
SAMPLERATE = 32000
    

class Player:
    def __init__(self):
        self.dac = DAC(Pin(25))
        self.square = [0, 255]
        self.frq = 1
        self.counter = 0
        self.tim = Timer(0)
        self.tim.init(freq=SAMPLERATE, mode=Timer.PERIODIC, callback=self.ticker)
    
    def ticker(self, timer):
        self.counter += 1
        if self.counter >= SAMPLERATE:
            self.counter = 0

        self.play(self.frq)

    def play(self, frq=1):
        step = int(frq / SAMPLERATE * self.counter) % 2
        self.dac.write(step * 255)


import random, time 

dac = DAC(Pin(25))
seq = [100,200,400,800,1600]
volume = 5
val = 0

def play(timer):
    global val, volume 
    dac.write(val * volume)
    val = 1 - val 

t = Timer(0)

for f in range(100):
    t.init(freq=random.choice(seq), mode=Timer.PERIODIC, callback=play)
    time.sleep(0.1)

"""