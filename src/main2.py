    # ONLY FUNCTIONS THAT MATTER:
    # spyderbot.move_forward_smooth()
    # spyderbot.move_backward_smooth()
    # spyderbot.turn_left()
    # spyderbot.turn_right()
# Your robot library
from spyderbot_real import Spyderbot
import atexit

spyderbot = Spyderbot()
# makes shutdown function run when this program exits
atexit.register(spyderbot.shutdown)


while True:
    spyderbot.move_forward_smooth()
