# This is your main script.

import math 
from machine import Pin, DAC, Timer 

#sine = bytearray(2)

#for i in range(len(sine)):
#    sine[i] = 128 + int(127 * math.sin(2 * math.pi * i / len(sine)))


"""
class Player:
    def __init__(self):
        self.dac = DAC(Pin(25))
        self.square = [0, 255]
        self.frq = 1000
        self.counter = 0
        self.tim = Timer(0)
        self.tim.init(freq=SAMPLERATE, mode=Timer.PERIODIC, callback=self.ticker)
    
    def ticker(self, timer):
        self.counter += 1
        if self.counter >= SAMPLERATE:
            self.counter = 0

        self.play()

    def play(self):
        step = int(self.frq / (SAMPLERATE * 2) * self.counter) % 2
        self.dac.write(step * 255)
"""

import random, time 

size = 64
dac = DAC(Pin(25))
sine = bytearray(size)

for i in range(size):
    sine[i] = 128 + int(127 * math.sin(2 * math.pi * i / size))

idx = 0


def play(timer):
    #global idx  
    for v in sine:
        #dac.write(sine[idx])
        dac.write(v)
    #idx += 1
    #if idx >= size:
    #    idx = 0

t = Timer(0)

t.init(freq=2000, mode=Timer.PERIODIC, callback=play) 


