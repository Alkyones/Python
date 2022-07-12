from datetime import datetime
import time
import sched
import os,sys


folderPath = sys.argv[1]

scheduler = sched.scheduler(time.time, time.sleep)

def FileCounter(folderName):
    date_today = datetime.now().strftime('%Y-%m-%d')
    hour_today = datetime.now().strftime('%H:%M')
    _str = f"{date_today}\t{hour_today}\n{folderName}\t"

    ## check files
    counter_file,counter_dir, etc = 0,0,0
    for file in os.listdir(folderPath):
        if os.path.isfile(os.path.join(folderPath,file)):
            counter_file += 1
        elif os.path.isdir(os.path.join(folderPath,file)):
            counter_dir += 1
        else:
            etc += 1
    
    #format str
    if counter_file > 0:
        _str += f"has {counter_file} file(s)\t"
    
    if counter_dir > 0:
        _str += f"has {counter_dir} folder(s)\t"

    if etc > 0:
        _str += f"has {etc} unknown type file(s)\t"


    print(_str)


    




    print (_str)
    scheduler.enter(3600, 1, FileCounter, kwargs={'folderName': folderPath})


scheduler.enter(1, 1, FileCounter, kwargs={'folderName': folderPath}) 
scheduler.run()


FileCounter(folderPath)






