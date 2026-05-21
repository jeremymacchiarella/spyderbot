from spyderbot_real import Spyderbot
import atexit
import time


def main():
    spyderbot = Spyderbot()
    time.sleep(1)


    # ONLY FUNCTIONS THAT MATTER:
    # spyderbot.move_forward_smooth()
    # spyderbot.move_backward_smooth()
    # spyderbot.turn_left()
    # spyderbot.turn_right()

    # makes shutdown function run when this program exits
    atexit.register(spyderbot.shutdown)


    for i in range(10):
        spyderbot.move_backward_smooth()
    
    time.sleep(1)



if __name__ == "__main__":
    main()
