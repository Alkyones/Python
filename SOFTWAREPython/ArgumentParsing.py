# internal arguement parsing
def randomFunction(*args, **kwargs):
    print(args[0])
    print(args[1])
    print(args[2])
    print(args[3])
    print(kwargs['KeyOne'])
    print(kwargs['KeyTwo'])


#randomFunction(1, 2, 3, 4, KeyOne="test", KeyTwo="died")

#external arguement parsing
# import sys
# print(sys.argv[0])
# print(sys.argv[1])

# file creator
import sys
filename  = sys.argv[1]

with open(filename, 'w') as f:
    f.write("")
    f.close()


