from spyderbot_real import Spyderbot
import atexit
import time


def main():
    spyderbot = Spyderbot()
    time.sleep(1)

    # makes shutdown function run when this program exits
    atexit.register(spyderbot.shutdown)

    spyderbot.move_leg_forward_smooth(10,11)
    time.sleep(1)



if __name__ == "__main__":
    main()
