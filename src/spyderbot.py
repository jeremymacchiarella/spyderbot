from adafruit_servokit import ServoKit
import time
import sys


class Spyderbot:

    def __init__(self):

        # knees are even and hips are odd
        # knees init to 60 and hips init to 90
        self.SERVO_INIT_ANGLES = [60,90,60,90,60,90,60,90,60,90,60,90]
        self.kit = ServoKit(channels=16) # keep at 16 even though we use 12
        self.init_servo_pos()


    def init_servo_pos(self):
        for i in range(12):
            self.kit.servo[i].angle = self.SERVO_INIT_ANGLES[i]

    def move_servo_slow(self, servo_idx, target_angle): # not tested yet
        step = 2
        delay = 0.01

        current_angle = self.kit.servo[servo_idx].angle
        if current_angle is None:
            print(f"Error: Servo {servo_idx} angle is None. Cannot move servo, exiting")
            sys.exit()

        while abs(current_angle - target_angle) > 0:
            if current_angle < target_angle:
                current_angle = min(current_angle + step, target_angle)
            else:
                current_angle = max(current_angle - step, target_angle)

            self.kit.servo[servo_idx].angle = current_angle
            time.sleep(delay)

    def move_servo_slow_delta(self, servo_idx, delta):
        

        current_angle = self.kit.servo[servo_idx].angle
        goal = int(current_angle + delta)
        
        if (goal > 180 or goal < 0):
            print(f"error: trying to set invalid servo {servo_idx} angle, exiting")
            sys.exit()

        self.move_servo_slow(servo_idx, goal)

    def move_servo(self, servo_idx, target_angle):
        if (target_angle > 180 or target_angle < 0):
            print(f"error: trying to set invalid servo {servo_idx} angle, exiting")
            sys.exit()

        self.kit.servo[servo_idx].angle = target_angle

    def move_servo_delta(self, servo_idx, delta):
        current_angle = self.kit.servo[servo_idx].angle
        goal = int(current_angle + delta)
        
        if (goal > 180 or goal < 0):
            print(f"error: trying to set invalid servo {servo_idx} angle, exiting")
            sys.exit()

        self.kit.servo[servo_idx].angle = goal

    def lift_knee(self, servo_idx):
        self.move_servo(servo_idx, 120)

    

    def lower_knee(self, servo_idx):
        self.move_servo(servo_idx, 64)

    def move_hip_forward(self, servo_idx):
        if (servo_idx > 5):
            self.move_servo_delta(servo_idx, -50)
        else:
            self.move_servo_delta(servo_idx, 50)

    def move_hip_middle(self, servo_idx):
        self.move_servo(servo_idx, 90)

    def move_hip_backward(self, servo_idx):
        if (servo_idx > 5):
            self.move_servo_delta(servo_idx, 50)
        else:
            self.move_servo_delta(servo_idx, -50)

    def lift_knee_slow(self, servo_idx):
        self.move_servo_slow(servo_idx, 120)

    def lower_knee_slow(self, servo_idx):
        self.move_servo_slow(servo_idx, 64) 
    
    def move_hip_forward_slow(self, servo_idx):
        if (servo_idx > 5):
            self.move_servo_slow_delta(servo_idx, -30)
        else:
            self.move_servo_slow_delta(servo_idx, 30)

    def move_hip_backward_slow(self, servo_idx):
        if (servo_idx > 5):
            self.move_servo_slow_delta(servo_idx, 30)
        else:
            self.move_servo_slow_delta(servo_idx, -30)

    def move_servos_slow_group(self, servo_targets, step=2, delay=0.01):

        current_angles = {}
        for servo_idx, target in servo_targets:
            angle = self.kit.servo[servo_idx].angle
            if angle is None:
                print(f"Error: Servo {servo_idx} angle is None")
                sys.exit()
            current_angles[servo_idx] = angle

        done = False

        while not done: 
            done = True
            for servo_idx, target in servo_targets:
                current = current_angles[servo_idx]

                if abs(current - target) > 0:
                    done = False

                    if current < target:
                        current = min(current + step, target)
                    else:
                        current = max(current - step, target)

                    self.kit.servo[servo_idx].angle = current
                    current_angles[servo_idx] = current

            time.sleep(delay)

    
    def move_servos_slow_group_delta(self, servo_deltas, step=2, delay=0.01):
        servo_targets = []

        for servo_idx, delta in servo_deltas:
            current = self.kit.servo[servo_idx].angle

            if current is None: 
                print(f"Error: Servo {servo_idx} angle is None")
                sys.exit()

            goal = int(current + delta)

            if goal > 180 or goal < 0:
                print(f"error: invalid target for servo {servo_idx}")
                sys.exit()

            servo_targets.append((servo_idx, goal))

        self.move_servos_slow_group(servo_targets, step, delay)

            
        


    def lift_knees_group(self, side):
        if (side == 'right'):
            self.move_servos_slow_group([(0, 120),(4, 120),(8, 120)])

        if (side == 'left'):
            self.move_servos_slow_group([(2, 120),(6, 120),(10, 120)])

    def lower_knees_group(self, side):
        if (side == 'right'):
            self.move_servos_slow_group([(0, 60),(4, 60),(8, 60)])

        if (side == 'left'):
            self.move_servos_slow_group([(2, 60),(6, 60),(10, 60)])

    def move_hips_forward_group(self, side):
        if (side == 'right'):
            self.move_servos_slow_group_delta([(1, -50),(5, -50),(9, -50)])

        if (side == 'left'):
            self.move_servos_slow_group_delta([(3, 50),(7, 50),(11, 50)])

    def move_hips_backward_group(self, side):
        if (side == 'right'):
            self.move_servos_slow_group_delta([(1, 50),(5, 50),(9, 50)])

        if (side == 'left'):
            self.move_servos_slow_group_delta([(3, -50),(7, -50),(11, -50)])

    

    
    
    

    


    def shutdown(self):
        for i in range(12):
            # stop sending pwm signals to servos
            self.kit.servo[i].angle = None

        

        


