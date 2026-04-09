from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)

for i in range(0,12,2):
    kit.servo[i].angle = 100
    time.sleep(1)
    kit.servo[i].angle = 20
    time.sleep(1)
    kit.servo[i].angle = 60
    time.sleep(1)
for i in range(1,13,2):
   kit.servo[i].angle = 130
   time.sleep(1)
   kit.servo[i].angle = 50
   time.sleep(1)
   kit.servo[i].angle = 90
   time.sleep(1)

