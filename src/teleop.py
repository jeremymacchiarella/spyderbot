import curses
import time

def main(stdscr):
    stdscr.nodelay(True)  # non-blocking input

    while True:
        key = stdscr.getch()

        if key == ord('w'):
            print("forward")

        elif key == ord('a'):
            print("turn left")

        elif key == ord('d'):
            print("turn right")

        elif key == ord('s'):
            print("backward")

        elif key == ord('q'):
            break

        time.sleep(0.05)

curses.wrapper(main)