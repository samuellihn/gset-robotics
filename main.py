#!/usr/bin/env python3
from ev3dev.ev3 import *
# from simple_pid import PID

us=UltrasonicSensor()
us.mode='US-DIST-CM'
mb = LargeMotor('outB')
mc = LargeMotor('outC')

# # PID
# pid = PID(1, 0.1, 0.05, setpoint=1)

#Start Loop
target=300
while True:
  dist=us.value()
  if dist == target:
     mb.stop(stop_action='hold')
     mc.stop(stop_action='hold')
  elif dist > target:
     mb.run_forever(speed_sp=min(900,3*(dist-target)))
     mc.run_forever(speed_sp=min(900,3*(dist-target)))
  else:
     mb.run_forever(speed_sp=max(-900,3*(dist-target)))
     mc.run_forever(speed_sp=max(-900,3*(dist-target)))