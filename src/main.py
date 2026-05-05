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
        spyderbot.move_forward()
        
    time.sleep(1)



if __name__ == "__main__":
    main()
