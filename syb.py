
import subprocess
import os, sys
from subprocess import Popen, CREATE_NEW_CONSOLE

#Add differentiation between windows and linux machines
if sys.platform == "darwin":
    #apple mac
    pass
elif sys.platform.startswith("win"):
    pass


def check_if_pull_needed():
    if ['fast-forwared' in sys.argv[4]]:
        #pull needed for fast-forward compatibility
        Popen("git pull", creationflags=CREATE_NEW_CONSOLE)   # git pull after checkout



def change_branch(path, branchName):
    path = os.environ.get('FRUPRO') + '\\' + path
    oldcwd = os.getcwd()

    branchCode = f'git checkout {branchName}'
    os.chdir(path)
    Popen("git pull", creationflags=CREATE_NEW_CONSOLE)   # git pull before checkout
    Popen(branchCode)  # git checkout 
    
    os.chdir(oldcwd)


change_branch("produce-service", "staging")





