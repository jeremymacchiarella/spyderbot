import curses
import time
from spyderbot import Spyderbot
import atexit

def main(stdscr):
    stdscr.nodelay(True)
    spyderbot = Spyderbot()
    time.sleep(1)

    # makes shutdown function run when this program exits
    atexit.register(spyderbot.shutdown)

    while True:
        key = stdscr.getch()

        if key == ord('w'):
            spyderbot.move_forward()

        elif key == ord('a'):
            spyderbot.turn_left()

        elif key == ord('d'):
            spyderbot.turn_right()

        

       
        time.sleep(0.05)


if __name__ == "__main__":
    curses.wrapper(main)