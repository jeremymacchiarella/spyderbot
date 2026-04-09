from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)

for i in range(12):
    kit.servo[i].angle = None
