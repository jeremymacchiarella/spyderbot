from spyderbot import Spyderbot
import atexit
import time
import keyboard


def main():
    #spyderbot = Spyderbot()
    time.sleep(1)

    # makes shutdown function run when this program exits
    #atexit.register(spyderbot.shutdown)

    while (1):
        if keyboard.is_pressed('w'):
            print("forward")
    
        elif keyboard.is_pressed('a'):
            print("turn left")
    
        elif keyboard.is_pressed('d'):
            print("turn right")
    
        elif keyboard.is_pressed('s'):
            print("backward")

    
        
    time.sleep(1)



if __name__ == "__main__":
    main()
