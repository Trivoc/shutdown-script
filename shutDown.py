import time
import timeInput
import sys
import signal
from platform import system as os
from subprocess import call

def signal_handler(signal, frame):
        print('\nCancelling shutdown')
        sys.exit(0)

def sleepLoop(remainder) : 
    while remainder  > 0 :
        print("    Remaining: " + timeInput.formattedTimeString(remainder-1) + "    ", end='\r')
        time.sleep(1)
        remainder -= 1
    print("\nTime up!")

def shutDown() :
    print("Turning off...")
    if (os() == "Linux") : 
        print("welp") #debugging...
        #call(["systemctl poweroff", "-i"]) 
    if (os() == "Windows") :
        print("welp2")
        #call(["shutdown", "/s"])

def inputTime() : 
    limitStr = input("How long until shutdown? (X Y Z (hours minutes seconds), or q to quit) \n")

    if(limitStr == ("q" or "Q" or "")) : 
        print("No time given, quitting!")
        quit()
    else : 
        specTime = timeInput.getTime(limitStr)
        print("Setting time to " + timeInput.formattedTimeString(specTime) + "\n")
        sleepLoop(specTime)
        shutDown()

args = sys.argv
signal.signal(signal.SIGINT, signal_handler)
if(len(args) > 1) : 
    sleepLoop(timeInput.getTime(str(args[1:])))
else : 
    inputTime()
shutDown()


