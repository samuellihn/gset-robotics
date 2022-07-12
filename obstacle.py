#!/usr/bin/python3

from ev3dev.ev3 import *
from time import sleep

usSensor = UltrasonicSensor()
drive_l = LargeMotor('outB')
drive_r = LargeMotor('outC')

while True:
    distance = usSensor.distance_centimeters
    print(distance)

    if(distance < 15):
        drive_r.run_forever(speed_sp=900)
        drive_l.run_forever(speed_sp=-900)
