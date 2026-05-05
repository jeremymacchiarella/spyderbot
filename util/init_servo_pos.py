from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)

for i in range(1, 13, 2):
    kit.servo[i].angle = 90