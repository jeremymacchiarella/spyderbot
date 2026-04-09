from adafruit_servokit import ServoKit
import time
import sys


SERVO_INIT_ANGLES = []
kit = ServoKit(channels=16)


def main():

    pass

    

def init_servo_pos():
    for i in range(12):
        kit.servo[i].angle = SERVO_INIT_ANGLES[i]

def move_servo_slow(servo_idx, target_angle):
    step = 1
    delay = 0.02

    current_angle = kit.servo[servo_idx].angle
    if current_angle is None:
        print(f"Error: Servo {servo_idx} angle is None. Cannot move servo.")
        sys.exit()

    while abs(current_angle - target_angle) > 0:
        if current_angle < target_angle:
            current_angle = min(current_angle + step, target_angle)
        else:
            current_angle = max(current_angle - step, target_angle)

        kit.servo[servo_idx].angle = current_angle
        time.sleep(delay)







if __name__ == "__main__":
    main()