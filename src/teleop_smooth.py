import curses
import time
from spyderbot import Spyderbot
import atexit


def main(stdscr):
    curses.cbreak() # read key press instantly
    stdscr.nodelay(True) #  doesn't block, return -1 if no key pressed
    stdscr.keypad(True) # enable keyboard keys

    spyderbot = Spyderbot() # Initialize robot
    time.sleep(1) # wait for 1sec 
    atexit.register(spyderbot.shutdown) # servos turn off when program exits

    def flush_keys():
        while (stdscr.getch() != -1):
            pass
    try:
        while True:
                key = stdscr.getch()

                #Forward
                if key == ord('w'):
                    spyderbot.move_forward_smooth()
                    flush_keys()
                elif key == ord('q'):
                    break
                time.sleep(0.2)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    curses.wrapper(main)

