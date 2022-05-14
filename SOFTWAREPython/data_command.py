from abc import ABCMeta, abstractstaticmethod
from faker import Faker
import sqlite3

# Abstract Base database
# cmain = sqlite3.connect('test.db')
# c = cmain.cursor()
# c.execute("""CREATE TABLE IF NOT EXISTS person(id INTEGER PRIMARY KEY,name TEXT, age INTEGER)""")
# cmain.commit()
# cmain.close()

# Receiver
class Person:
    def __init__(self):
        self.faker = Faker()
        self.connection = sqlite3.connect('test.db')

    def add_person(self):
        c = self.connection.cursor()
        c.execute("""INSERT INTO person(name, age) VALUES(?, ?)""",
                  (self.faker.name(), self.faker.random_int(min=18, max=80)))
        print("Person has added.")
        self.connection.commit()
    def remove_person(self):
        c = self.connection.cursor()

        # info of deleted person
        deleted_person = c.execute("""SELECT * FROM person WHERE id=(SELECT MAX(id) FROM person)""")
        deleted_person = deleted_person.fetchone()
        self._removed_person = deleted_person
        c.execute("""DELETE FROM person WHERE id =(SELECT MAX(id) FROM person)""")
        self.connection.commit()
        print(f"Person has removed {self._removed_person} ")        
        

# IClass which is the main factor class


class ICommand(metaclass=ABCMeta):

    @abstractstaticmethod
    def execute():
        """Static method has inheritences"""

# command class 1
class personAddCommand(ICommand):
    def __init__(self, person):
        self._person = person
    def execute(self):
        self._person.add_person()
# command class 2
class personRemoveCommand(ICommand):

    def __init__(self, person):
        self._person = person
        self._removed_person = None # removed person

    def execute(self):
        self._person.remove_person()

# invoker class
class Controller:
    """The invoker class"""

    def __init__(self):
        self._commands = {}
        self._history = []
        self._records = sqlite3.connect('test.db').cursor()

    def register(self, command_name, command):
        self._commands[command_name] = command

    def execute(self, command_name):
        if command_name in self._commands:
            self._commands[command_name].execute()
            self._history.append(command_name)
        else:
            print("Command not found")
    
    def redo(self):
        if len(self._history) > 0:
            command_name =  self._history.pop()
            if command_name in self._commands:
                print("Command {} has been undone".format(command_name))
                self.execute(command_name)
                self._history.pop()
            else:
                print("Command not found")

    @property
    def records(self):
        data = self._records.execute("""SELECT * FROM person""")
        return data.fetchall()

    @property
    def history(self):
        return self._history


# client
if __name__ == "__main__":
    # receiver
    PERSON = Person()

    # commands
    ADD_COMMAND = personAddCommand(PERSON)
    REMOVE_COMMAND = personRemoveCommand(PERSON)
    # invoker
    CONTROLLER = Controller()

    # register commands
    CONTROLLER.register("add", ADD_COMMAND)
    CONTROLLER.register("remove", REMOVE_COMMAND)

    # execute commands
    #CONTROLLER.execute("add")
    #CONTROLLER.execute("remove")
    #CONTROLLER.redo()

    # print history
    print(CONTROLLER.history)
    print(CONTROLLER.records)