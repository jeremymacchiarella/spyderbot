from spyderbot import Spyderbot
import atexit
import time


def main():
    spyderbot = Spyderbot()

    spyderbot.move_servo_slow(0, 120)
    print("done with slow move")
    time.sleep(1)
    spyderbot.move_servo(0, 60)

    

    # makes shutdown function run when this program exits
    atexit.register(spyderbot.shutdown)



if __name__ == "__main__":
    main()
