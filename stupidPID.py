#!/usr/bin/python3

import time
from ev3dev.ev3 import *
from simple_pid import PID
from utils import *

mb = LargeMotor('outA')
mc = LargeMotor('outD')

cl = ColorSensor()
cl.mode = 'COL-REFLECT'

# PID
# pid = PID(0.020, 0.00005, 0.0, setpoint=0)
KP, KI, KD = 0.01, 0.00005, 0.0018
print(KP, KI, KD)
pid = PID(KP, KI, KD, setpoint=0)
pid.output_limits = (-1.0, 1.0)

# follow right side of line
DESIRED_LINE = 50

while True:
    light = cl.value()
    error = DESIRED_LINE - light

    v = pid(error)
    print(v)

    right, left = vec2_to_tank((v, 0.5))

    mb.run_forever(speed_sp=right)
    mc.run_forever(speed_sp=left)
