from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)

for i in range(0, 12, 2):
    kit.servo[i].angle = 120
    time.sleep(1)

