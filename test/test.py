from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)

kit.servo[0].angle = 90
kit.servo[2].angle = 90

