import os
import time

#os run docker stats
while 1:
    cmdStr = "docker stats --no-stream valerie_mongo > file.txt" 
    os.system(cmdStr)
    time.sleep(3)

