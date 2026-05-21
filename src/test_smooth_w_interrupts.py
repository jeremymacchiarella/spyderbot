from spyderbot_real import Spyderbot
import atexit
import time


def main():
    spyderbot = Spyderbot()
    time.sleep(1)

    # makes shutdown function run when this program exits
    atexit.register(spyderbot.shutdown)

    while (1):
        spyderbot.move_forward_smooth()
    time.sleep(1)



if __name__ == "__main__":
    main()
