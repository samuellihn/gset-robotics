#!/usr/bin/env python3
import time

from ev3dev.ev3 import *
from simple_pid import PID
from utils import *


mc = LargeMotor('outB')
mb = LargeMotor('outC')

cl = ColorSensor()
cl.mode='COL-REFLECT'

lcd = Screen()

# PID
pid = PID(1, 0.1, 0.05, setpoint=50)

def func(x):
    return (1/(-x - 1) + 1) * 2

#follow right side of line
ideal = 50
defaultMotorValue = 200
count = 0

while True:
    light = cl.value()
    offset = (light - ideal)/50
    print(offset)
    if abs(offset) <= 0.1:
       count = 0
    elif abs(offset) > 0.1 and count < defaultMotorValue:
       count += 2
    turnSideValue = int(defaultMotorValue - func(abs(offset)) * defaultMotorValue - count)
    print(turnSideValue)

    if offset < 0:
        mc.run_forever(speed_sp=turnSideValue)
        mb.run_forever(speed_sp=defaultMotorValue)
    else:
        mb.run_forever(speed_sp=turnSideValue)
        mc.run_forever(speed_sp=defaultMotorValue)

    #mb.run_forever(speed_sp=pid(light))
    #mc.run_forever(speed_sp=pid(light))

