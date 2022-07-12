#!/usr/bin/python3

import time
from ev3dev.ev3 import *
from simple_pid import PID
from utils import *

drive_l = LargeMotor('outB')
drive_r = LargeMotor('outC')
cl = ColorSensor()
cl.mode = 'COL-REFLECT'

# THIS WORKS PLEASE DONT DELETE
# THIS WORKS PLEASE DONT DELETE
# THIS WORKS PLEASE DONT DELETE
# THIS WORKS PLEASE DONT DELETE
# THIS WORKS PLEASE DONT DELETE
# THIS WORKS PLEASE DONT DELETE
# THIS WORKS PLEASE DONT DELETE
# THIS WORKS PLEASE DONT DELETE
# THIS WORKS PLEASE DONT DELETE
# THIS WORKS PLEASE DONT DELETE

# There's no kI in team ~said no one ever

# PID
# KP, KI, KD = 0.04, 0.00005, 0.02
KP, KI, KD = 0.038, 0.00005, 0.001
# KP, KI, KD = 0.03, 0.0000, 0.0

# KP, KI, KD = 0.011, 0.00005, 0.0018
print(KP, KI, KD)
pid = PID(KP, KI, KD, setpoint=0)
pid.output_limits = (-1.0, 1.0)

# follow right side of line
DESIRED_LINE = 50
count = 0

hasReachedRed = False

def lineFollowing(light):
    error = DESIRED_LINE - light
    v = pid(error)

    throttle = abs(1 - pow(v, 2))
    print(v, throttle)

    right, left = vec2_to_tank((v, throttle))

    drive_r.run_forever(speed_sp=right)
    drive_l.run_forever(speed_sp=left)

while True:
    light = cl.value()

    if cl.value() >= 56 and cl.value() <= 61:
        hasReachedRed = True

    if not hasReachedRed:
        lineFollowing(light)
    else:
        drive_r.stop()
        drive_l.stop()
        print("YAY!")

