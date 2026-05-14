import curses
import time
from spyderbot import Spyderbot
import atexit

current_command = None


def main(stdscr):
    current_command = None
    last_w_time = 0
    W_RELEASE_TIMEOUT = 0.15  # seconds without w means released

    curses.cbreak() # read key press instantly
    stdscr.nodelay(True) #  doesn't block, return -1 if no key pressed
    stdscr.keypad(True) # enable keyboard keys

    spyderbot = Spyderbot() # Initialize robot
    time.sleep(1) # wait for 1sec 
    atexit.register(spyderbot.shutdown) # servos turn off when program exits

    def interrupted():
        nonlocal current_command
        nonlocal last_w_time
        key = stdscr.getch() # read key

        # No key pressed
        if key == -1:
            if current_command == "forward":
                if time.time() - last_w_time > W_RELEASE_TIMEOUT:
                    current_command = None # Stop moving forward
                    return True # interrupt movement
            elif current_command == "left":
                if time.time() - last_w_time > W_RELEASE_TIMEOUT:
                    current_command = None # Stop turning left
                    return True # interupt movement
            elif current_command == "right":
                if time.time() - last_w_time > W_RELEASE_TIMEOUT:
                    current_command = None # Stop turning right
                    return True # interupt movement
            return False

        # w key is pressed
        if key == ord('w'):
            last_w_time = time.time() # record the time w was pressed
            current_command = "forward"
            return False # no interruption

        elif key == ord('a'):
            last_w_time = time.time() # record the time a was pressed
            current_command = "left"
            return False # no interruption

        elif key == ord('d'):
            last_w_time = time.time() # record the time d was pressed
            current_command = "right"
            return False # no interruption

        elif key == ord('q'):
            raise KeyboardInterrupt

        return False

    try:
        while True:
            key = stdscr.getch() # Read key

            # Check which key is pressed and set the last pressed time
            if key == ord('w'):
                current_command = "forward"
                last_w_time = time.time()
            elif key == ord('a'):
                current_command = "left"
                last_w_time = time.time()
            elif key == ord('d'):
                current_command = "right"
                last_w_time = time.time()
            elif key == ord('q'):
                break
            elif key == -1: # See which key was pressed and then released, record the time, and set the command to None
                if current_command == "forward":
                    if time.time() - last_w_time > W_RELEASE_TIMEOUT:
                        current_command = None
                elif current_command == "left":
                    if time.time() - last_w_time > W_RELEASE_TIMEOUT:
                        current_command = None 
                elif current_command == "right":
                    if time.time() - last_w_time > W_RELEASE_TIMEOUT:
                        current_command = None

            if current_command == "forward":
                spyderbot.move_forward(interrupted)
            elif current_command == "left":
                spyderbot.turn_left(interrupted)
            elif current_command == "right":
                spyderbot.turn_right(interrupted)

            time.sleep(0.02)

    except KeyboardInterrupt:
        pass
        time.sleep(0.02)

if __name__ == "__main__":
    curses.wrapper(main)

