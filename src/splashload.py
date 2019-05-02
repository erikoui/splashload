#!/usr/bin/env python3

# use lowercase for variables
import cv2
import subprocess
import time

# User Variables
# TODO: get processname and other options from argparser or similar
processname = 'polo-gtk'
timelimit=10 # seconds
checkperiod=0.5 # seconds
threshold=0.005 # times total mem
stoppedlimit=3
resolution=[1366,768]
width=400
height=250
x=int(resolution[0]/2-width/2)
y=int(resolution[1]/2-height/2)

# Script Variables
totaltime=0
cmd = ['ps', '-C', processname, '-o','vsz']
prevmem=0
stoppedcounter=0

# Show Splash
img=cv2.imread('image.jpg')
cv2.imshow('Loading',cv2.resize(img,(width,height)))
cv2.moveWindow('Loading',x,y)
cv2.resizeWindow('Loading',width,height)
cv2.waitKey(1)

# Main Loop
while totaltime < timelimit:
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    o,e = process.communicate()

    output = o.decode('ascii')
    errors = e.decode('ascii')
    returncode = process.returncode
    #print('Output:' + output)
    #print('Error: ' + errors)
    #print('Code: ' + returncode)
    if returncode == 0:#process was found
        totalmem = 0
        mems = output.split('\n')[1:-1]
        for mem in mems:
            totalmem += int(mem)
        print('Total memory:' + str(totalmem) + 'KB')
        print("Prev mem:" + str(prevmem) + ". Total mem:" + str(totalmem))
        if totalmem-prevmem < (threshold*totalmem):
            print("Stopped Loading")
            stoppedcounter += 1
        else:
            stoppedcounter = 0
            print("Still Loading")
        prevmem = totalmem
    else:
        print('Return code not 0')
        stoppedcounter += 1

    if stoppedcounter >= stoppedlimit:
        break
    time.sleep(checkperiod)
    totaltime += checkperiod
cv2.destroyAllWindows()
