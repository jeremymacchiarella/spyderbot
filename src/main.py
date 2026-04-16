from spyderbot import Spyderbot
import atexit


def main():
    spyderbot = Spyderbot()

    # makes shutdown function run when this program exits
    atexit.register(spyderbot.shutdown)

    spyderbot.lift_knee(0)
    spyderbot.move_hip_forward(1)
    spyderbot.lower_knee(0)
    spyderbot.move_hip_backward(1)




if __name__ == "__main__":
    main()