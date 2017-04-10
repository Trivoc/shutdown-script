import platform
import time
import timeInput
from sys import stdout
from subprocess import call

def sleepLoop(remainder) : 
    while remainder  > 0 :
        print("    Remaining: " + timeInput.formattedTimeString(remainder) + "    ", end='\r')
        time.sleep(1)
        remainder -= 1
    stdout.flush()
    print("\nTime up!")


def countDown(seconds) : 
    part = seconds % 10
    time.sleep(part)
    seconds = seconds - part
    seconds = sleepLoop(3600, seconds)
    seconds = sleepLoop(300, seconds)
    seconds = sleepLoop(10, seconds)
    print("\nTime up!")

if (platform.system() == "Linux") : 
    print("Identified Linux platform")

limitStr = input("How long until shutdown? (X Y Z (hours minutes seconds), or q to quit) \n")

if(limitStr == ("q" or "Q" or "")) : 
    print("No time given, quitting!")
    quit()
else : 
    specTime = timeInput.getTime(limitStr)
    print("Setting time to " + timeInput.formattedTimeString(specTime) + "\n")
    call(["stty", "-echo"])
    sleepLoop(specTime)
    call(["stty", "echo"])




#subprocess.call(["shutdown", "/s"])	



