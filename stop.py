#!/usr/bin/python3

from ev3dev.ev3 import *

drive_l = LargeMotor('outB')
drive_r = LargeMotor('outC')


drive_r.run_forever(speed_sp=0)
drive_l.run_forever(speed_sp=0)
