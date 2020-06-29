import os

cmdStr = "ps -ef | grep valerie_stream | awk '{print $2}'"

pids = os.popen(cmdStr).read()

pidsList = pids.split("\n")

for pid in pidsList[0:len(pidsList)-1]:
    try:
    	os.kill(int(pid),9)
    except OSError:
    	pass

    #print(pid)

