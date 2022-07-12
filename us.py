#!/usr/bin/python3

from ev3dev.ev3 import *
colorSensor = ColorSensor()

usSensor = UltrasonicSensor()

while True:
    if(colorSensor.value() >= 56 and colorSensor.value() <= 61):
        print("DONE!")
    else:
        print(colorSensor.value())
    #print(usSensor.distance_centimeters)