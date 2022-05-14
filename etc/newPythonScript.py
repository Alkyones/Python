
from distutils import extension


filename = input('Enter a file name: ')
extension = filename.split('.')[-1]
with open(filename, 'w+') as f:
    if extension =="py":
        f.write("print('Hello world!')")
    elif extension == "js":
        f.write("console.log('Hello world!')")