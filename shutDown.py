import subprocess
import time

start = time.time()
print("Hello there!")



clock = time.time()
while (time.time() - start) < 5:
	inp = input("Want to quit?\n")
	if inp == "yes":
		break
	
print("Time out")
end = time.time()
print("Elapsed time: " + str((end - start)*1000000 ) + " ns")	


#subprocess.call(["shutdown", "/s"])	