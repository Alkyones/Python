import os, sys
seconds = 30



if len(sys.argv) == 2:
    if(sys.argv[1].isdigit()):
        seconds = int(sys.argv[1])
        
    if(sys.argv[1] == 'c' or sys.argv[1] == 'C'):
        print("Shut down has been cancelled")
        os.system('shutdown /a')
        

print(f"Shutting down in {seconds} seconds")
os.system(f"shutdown /s /t {seconds}")