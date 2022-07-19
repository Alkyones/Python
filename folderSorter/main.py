from datetime import datetime
from itertools import count
import time
import sched
import os,sys


folderPath = sys.argv[1]

scheduler = sched.scheduler(time.time, time.sleep)

def FileCounter(folderName):
    date_today = datetime.now().strftime('%Y-%m-%d')
    hour_today = datetime.now().strftime('%H:%M')
    _str = f"{date_today}\t{hour_today}\n{folderName}\thas "

    content = {
    "file":
    {
        "count": 0,
        "extension_mono": "file",
        "extension_many": "files",
        "exec": os.path.isfile
    },
    "folder":
    {
        "count": 0,
        "extension_mono": "folder",
        "extension_many": "folders",
        "exec": os.path.isdir
    },
    "other":
    {
        "count": 0,
        "extension_mono": "other",
        "extension_many": "others",
    }
    }


    ## check files

    for file in os.listdir(folderPath):
        if content["file"]["exec"](os.path.join(folderPath,file)):
            content["file"]["count"] += 1
        elif content["folder"]["exec"](os.path.join(folderPath,file)):
            content["folder"]["count"] += 1
            
        else:
            content["etc"]["count"] += 1
            
    
    #format str
    for type_f in content:
        if content[type_f]["count"]:
            count = content[type_f]["count"]
            ext = content[type_f]["extension_mono"] if count == 1 else content[type_f]["extension_many"]

            _str += f"{count} {ext}\t"        


    print(_str)
    scheduler.enter(3600, 1, FileCounter, kwargs={'folderName': folderPath})


scheduler.enter(1, 1, FileCounter, kwargs={'folderName': folderPath})

scheduler.run()


FileCounter(folderPath)






