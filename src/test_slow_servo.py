import atexit
import time
from spyderbot import Spyderbot
def main():
    spyderbot = Spyderbot()

    spyderbot.move_servo_slow_delta(0, 90)
    time.sleep(1)
    spyderbot.move_servo_slow_delta(0, -90)
    time.sleep(2)

    

    # makes shutdown function run when this program exits
    atexit.register(spyderbot.shutdown)



if __name__ == "__main__":
    main()
