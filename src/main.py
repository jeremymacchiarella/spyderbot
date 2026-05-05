from spyderbot import Spyderbot
import atexit
import time


def main():
    spyderbot = Spyderbot()
    time.sleep(1)

    # makes shutdown function run when this program exits
    atexit.register(spyderbot.shutdown)

    #spyderbot.lift_knees_group('left')
    for i in range(10):

        # spyderbot.turn_right()
        spyderbot.turn_right()
        # spyderbot.lift_knee_slow(0)
        # spyderbot.lift_knee_slow(4)
        # spyderbot.lift_knee_slow(8)

        

        # spyderbot.move_hips_forward_group_abs('left')

        # spyderbot.lower_knees_group('left')

        # spyderbot.lift_knees_group('right')

        # spyderbot.move_hips_backward_group_abs('left')

        # spyderbot.move_hips_forward_group_abs('right')

        # spyderbot.lower_knees_group('right')

        # spyderbot.lift_knees_group('left')

        # spyderbot.move_hips_backward_group_abs('right')

        



     


        

        # time.sleep(1)

       
        # time.sleep(0.2)
        # spyderbot.move_hip_forward_slow(1)
        # spyderbot.move_hip_forward_slow(5)
        # spyderbot.move_hip_forward_slow(9)
        # time.sleep(0.2)
        # spyderbot.lower_knee_slow(0)
        # spyderbot.lower_knee_slow(4)
        # spyderbot.lower_knee_slow(8)
        # time.sleep(0.2)
        # spyderbot.lift_knee_slow(2)
        # spyderbot.lift_knee_slow(6)
        # spyderbot.lift_knee_slow(10)
        # time.sleep(0.2)
        # spyderbot.move_hip_backward_slow(1)
        # spyderbot.move_hip_backward_slow(5)
        # spyderbot.move_hip_backward_slow(9)
        # time.sleep(0.2)
        # spyderbot.lower_knee_slow(2)
        # spyderbot.lower_knee_slow(6)
        # spyderbot.lower_knee_slow(10)
        # time.sleep(0.2)

    # spyderbot.lower_knees_group("left")
    time.sleep(1)



if __name__ == "__main__":
    main()
