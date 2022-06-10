from PersonCreator.createP import create_person

while True:
    want_to_add = input('do you want to add a person?(y/n)')
    if want_to_add == 'y':
        create_person()
    else:
        break