from datetime import datetime
import time
import sched
import os,sys


folderPath = sys.argv[1]

scheduler = sched.scheduler(time.time, time.sleep)

def FileCounter(folderName):
    counter = 0
    for file in os.listdir(folderName):
        if os.path.isdir(os.path.join(folderName,file)):
            counter += 1
            
    print (counter)
    
    scheduler.enter(30, 1, FileCounter, kwargs={'folderName': folderPath})


scheduler.enter(30, 1, FileCounter, kwargs={'folderName': folderPath}) 
scheduler.run()


FileCounter(folderPath)






