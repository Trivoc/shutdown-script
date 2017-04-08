import subprocess
import time

start = time.time()
print("Hello there!")

limitStr = input("How long until shutdown? (XXhYYmZZs) \n")
limit = int(limitStr)
if limit <= 10 : 
    time.sleep(limit)
else: 
    time.sleep(limit-10)
    print("10 seconds left")
    time.sleep(10)
print("Done!")

end = time.time()
print("Elapsed limit: " + str(end - start))

#subprocess.call(["shutdown", "/s"])	