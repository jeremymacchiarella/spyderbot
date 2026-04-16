from spyderbot import Spyderbot
import atexit
import time


def main():
    spyderbot = Spyderbot()
    time.sleep(1)

    # makes shutdown function run when this program exits
    atexit.register(spyderbot.shutdown)
    for i in range(10):
        spyderbot.lift_knee(0)
        spyderbot.lift_knee(4)
        spyderbot.lift_knee(8)
        time.sleep(0.5)
        spyderbot.move_hip_forward(1)
        spyderbot.move_hip_forward(5)
        spyderbot.move_hip_forward(9)
        time.sleep(0.5)
        spyderbot.lower_knee(0)
        spyderbot.lower_knee(4)
        spyderbot.lower_knee(8)
        time.sleep(0.5)
        spyderbot.lift_knee(2)
        spyderbot.lift_knee(6)
        spyderbot.lift_knee(10)
        time.sleep(0.5)
        spyderbot.move_hip_backward(1)
        spyderbot.move_hip_backward(5)
        spyderbot.move_hip_backward(9)
        time.sleep(0.5)
        spyderbot.lower_knee(2)
        spyderbot.lower_knee(6)
        spyderbot.lower_knee(10)
        time.sleep(0.5)



if __name__ == "__main__":
    main()
