import time
import timeInput
import sys
import signal
import flask
import threading
from platform import system as os
from subprocess import call

def signal_handler(signal, frame):
        print('\nCancelling shutdown')
        sys.exit(0)

def sleepLoop(remainder) : 
    while remainder  > 0 :
        print("    Remaining: " + timeInput.formatted_time_string(remainder) + "    ", end='\r')
        time.sleep(1)
        remainder -= 1
    print("\nTime up!")

def shutDown() :
    print("Turning off...")
    if (os() == "Linux") : 
        print("welp")
        #call(["systemctl poweroff", "-i"])
    if (os() == "Windows") :
        print("welp2")
        #call(["shutdown", "/s"])

def input_time () : 
    inp = input("How long until shutdown? (X Y Z (hours minutes seconds), or q to quit) \n")

    if(inp == ("q" or "Q" or "")) : 
        print("No time given, quitting!")
        quit()
    else : 
        seconds = timeInput.getTime(inp)
        print("Setting time to " + timeInput.formattedTimeString(seconds) + "\n")
        call(["stty", "-echo"])
        sleepLoop(seconds)
        call(["stty", "echo"])

def serverDaemon(password) : 
    print("Found password " + password)      

        

def setUpServer(password) : 
    d = threading.Thread(target=serverDaemon, args=(password, ))
    d.setDaemon(True)
    d.start()


setUpServer("password")
args = sys.argv
signal.signal(signal.SIGINT, signal_handler)
if(len(args) > 1) : 
    sleepLoop(timeInput.getTime(str(args[1:])))
else : 
    input_time()

shutDown()


