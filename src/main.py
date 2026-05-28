    # ONLY FUNCTIONS THAT MATTER:
    # spyderbot.move_forward_smooth()
    # spyderbot.move_backward_smooth()
    # spyderbot.turn_left()
    # spyderbot.turn_right()

import serial
import threading
import time

# Your robot library
from spyderbot_real import Spyderbot
import atexit

# Bluetooth serial connection
bt = serial.Serial("/dev/rfcomm0", 115200, timeout=0.05)

spyderbot = Spyderbot()
# makes shutdown function run when this program exits
atexit.register(spyderbot.shutdown)

# Button state flags
state = {
    "forward": False,
    "backward": False,
    "left": False,
    "right": False
}

# Thread-safe lock
lock = threading.Lock()


# -----------------------------
# Movement worker thread
# -----------------------------
def movement_loop():

    was_moving = False

    while True:

        with lock:
            forward = state["forward"]
            backward = state["backward"]
            left = state["left"]
            right = state["right"]

        moving = forward or backward or left or right

        if forward:
            was_moving = True
            spyderbot.move_forward_smooth()

        elif backward:
            was_moving = True
            spyderbot.move_backward_smooth()

        elif left:
            was_moving = True
            spyderbot.turn_left()

        elif right:
            was_moving = True
            spyderbot.turn_right()

        else:
            # Button released and movement finished
            if was_moving:
                spyderbot.init_servo_slow()
                was_moving = False

            time.sleep(0.01)


# Start movement thread
threading.Thread(target=movement_loop, daemon=True).start()


# -----------------------------
# Bluetooth command listener
# -----------------------------
while True:

    line = bt.readline().decode(errors="ignore").strip()

    if not line:
        continue

    print("Received:", line)

    with lock:

        if line == "FWD_ON":
            state["forward"] = True

        elif line == "FWD_OFF":
            state["forward"] = False

        elif line == "BACK_ON":
            state["backward"] = True

        elif line == "BACK_OFF":
            state["backward"] = False

        elif line == "LEFT_ON":
            state["left"] = True

        elif line == "LEFT_OFF":
            state["left"] = False

        elif line == "RIGHT_ON":
            state["right"] = True

        elif line == "RIGHT_OFF":
            state["right"] = False