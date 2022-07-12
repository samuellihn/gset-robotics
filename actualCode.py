#!/usr/bin/env python3
#house stuff!!

from ev3dev.ev3 import *
from time import sleep

drive_l = LargeMotor('outB')
drive_r = LargeMotor('outC')
us = UltrasonicSensor()
ir = InfraredSensor()
gy = GyroSensor()
gy.mode = 'GYRO-ANG'
us.mode = 'US_DIST_CM'

def ninety(leftright):
    gy.reset()
    if leftright:
        drive_r.runforever(speed_sp = -300)
        drive_l.runforever(speed_sp = 300)
    else:
        drive_l.runforever(speed_sp = 300)
        drive_r.runforever(speed_sp = -300)
    while (abs(gy.angle()) < 90):
        pass
    drive_r.brake()
    drive_l.brake()

max_ir_value = 0
prev_ir_value = 0

while(us.value() > 5):
    drive_r.runforever(speed_sp = 300)
    drive_l.runforever(speed_sp = 300)
drive_r.brake()
drive_l.brake()
ninety(True) # turn left 90


while(True):
    for i in range(3):
            # turn left three times in the corner, then turn right for each room
        while(us.value() > 5):
            drive_r.runforever(speed_sp=300)
            drive_l.runforever(speed_sp=300)
        drive_r.brake()
        drive_l.brake()
        drive_r.runforever(speed_sp=300)
        wait()
    while(us.value() > 5):
        drive_r.runforever(speed_sp=300)
        drive_l.runforever(speed_sp=300)
        drive_l.brake()
        wait()