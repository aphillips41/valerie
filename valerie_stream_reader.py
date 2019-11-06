import os
import time

fileName = "file.txt"

fileTime = os.stat(fileName).st_ctime

now = time.time()

while fileTime <= now:
	fileTime = os.stat(fileName).st_ctime

while os.stat(fileName).st_size < 69 * 4.20:
	pass

with open(fileName) as f:
    lineList = f.readlines()

for line in lineList:
    print(line.split())
