#!/usr/bin/python3

import time
from ev3dev.ev3 import *
from simple_pid import PID
from utils import *

drive_l = LargeMotor('outB')
drive_r = LargeMotor('outC')

drive_l.run_to_rel_pos(position_sp=198, speed_sp=500, stop_action="hold")
drive_r.run_to_rel_pos(position_sp=-198, speed_sp=500, stop_action="hold")


