from spyderbot import Spyderbot
import atexit


def main():
    spyderbot = Spyderbot()

    # makes shutdown function run when this program exits
    atexit.register(spyderbot.shutdown)



if __name__ == "__main__":
    main()