from abc import ABCMeta, abstractstaticmethod
import sqlite3
from faker import Faker

fakeD = Faker()

# Creating database


def new_conn(databaseName):
    conn = sqlite3.connect(databaseName)
    cursor = conn.cursor()
    # create if table is not exists
    cursor.execute("""CREATE TABLE IF NOT EXISTS table_settings(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            font_size INTEGER NOT NULL DEFAULT 14,
            font_color TEXT NOT NULL DEFAULT '#000000',
            font_weight INTEGER NOT NULL DEFAULT 400,
            background_color TEXT NOT NULL DEFAULT '#ffffff'
        )""")
    return conn


# Creating a html page with random table and default settings in css
default_settings = {
    'font_size': '14',
    'font_color': '#000000',
    'font_weight': '400',
    'background_color': '#ffffff',
}


def create_html_page(default_settings):
    faker = Faker()
    style = default_settings
    # create data
    data = []
    for i in range(10):
        data.append([faker.name(), faker.random_int(
            min=10, max=100), faker.city(), faker.email()])

    con = new_conn('CommandWebPage/database.db')
    cursor = con.cursor()
    cursor.execute(
        f"INSERT INTO table_settings(font_size, font_color, font_weight, background_color) VALUES ('{style['font_size']}', '{style['font_color']}', '{style['font_weight']}', '{style['background_color']}')")
    con.commit()
    # # Creating a table with random data
    with open('CommandWebPage/index.html', 'w') as f:
        f.write('''
        <!DOCTYPE html> 
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Table | User</title>
            <link rel="stylesheet" href="style.css">
        </head>
        <body>
            <center><h2>Atakan Yildirim KN-219i6e</h2></center>
            <table class='div-table'>
                <tr>
                    <th>Name</th>
                    <th>Age</th>
                    <th>City</th>
                    <th>Email</th>
                </tr>
        ''')
        for i in data:
            f.write('''
                <tr>
                    <td>{}</td>
                    <td>{}</td>
                    <td>{}</td>
                    <td>{}</td>
                </tr>
            '''.format(*i))
        f.write('''
            </table>
        </body>
        </html>
        ''')
    # create css
    # create css
    with open('CommandWebPage/style.css', 'w') as f:
        f.write(f'''
        table {{
                border-collapse: collapse;
                width: 100%;
                font-size: {style['font_size']}px;
                font-weight: {style['font_weight']};
                background-color: {style['background_color']};
            }}
            th, td {{
                text-align: left;
                padding: 8px;
            }}
            td {{color: {style['font_color']};}}
            tr:nth-child(even){{background-color: #f2f2f2}}
        ''')


# main class dedicated to abst
class ICommand(metaclass=ABCMeta):
    @abstractstaticmethod
    def execute():
        """Static method has inheritences"""


# Adding a new style command class 1
class NewStyle(ICommand):
    def __init__(self, classBase, settings):
        self._classBase = classBase
        self._conn = new_conn('CommandWebPage/database.db')
        self._settings = settings

    def execute(self):
        # call style method from classBase
        self._classBase.add_style(self._settings)

    def undo(self):
        self._classBase.rollback()

# Resetting the new style command class 2
class DefaultStyle(ICommand):
    def __init__(self, classBase):
        self._classBase = classBase
        self._conn = new_conn('CommandWebPage/database.db')
        self._settings = default_settings

    def execute(self):
        self._classBase.reset_style()  # call style method from classBase


# update style command class 3
class UpdateStyle(ICommand):
    def __init__(self, classBase):
        self._classBase = classBase
        self._conn = new_conn('CommandWebPage/database.db')

    def execute(self):
        self._classBase.update_style()  # call style method from classBase


# receiver class
class Table:
    def __init__(self):
        self._conn = new_conn('CommandWebPage/database.db')

    def add_style(self, settings):
        self._conn.cursor().execute("""INSERT INTO table_settings(font_size,font_color,font_weight,background_color) VALUES(?,?,?,?)""",
                                    (settings['font_size'], settings['font_color'], settings['font_weight'], settings['background_color']))
        self._conn.commit()
        print(f'Style is changed to {settings}')

    def reset_style(self):
        self._conn.cursor().execute("""UPDATE table_settings SET font_size = ?, font_color = ?, font_weight = ?, background_color = ?""",
                                    (default_settings['font_size'], default_settings['font_color'], default_settings['font_weight'], default_settings['background_color']))
        self._conn.commit()
        print(f'Style is resetted')

    def rollback(self):
        self._conn.cursor().execute(
            """DELETE FROM table_settings WHERE id =(SELECT max(id) FROM table_settings)""")
        self._conn.commit()
        print(f'Style is rollbacked')


# invoker class
class Controller:
    def __init__(self):
        self._commands = {}
        self._history = []
        self._conn = new_conn('CommandWebPage/database.db')

    def add_command(self, commandName, command):
        self._commands[commandName] = command

    def execute_command(self, commandName):
        self._history.append(commandName)
        self._commands[commandName].execute()

    #Applying the changes to the html page
    def update_style(self):
            style = new_conn('CommandWebPage/database.db').cursor().execute(
                "SELECT * FROM table_settings WHERE id=(SELECT max(id) FROM table_settings) ").fetchone()

            print(style)
            with open('CommandWebPage/style.css', 'w') as f:
                f.write(f'''
                table {{
                    border-collapse: collapse;
                    width: 100%;
                    font-size: {style[1]}px;
                    font-weight: {style[3]};
                }}
                th, td {{
                    text-align: left;
                    padding: 8px;
                }}
                td {{color: {style[2]};}}
                tr:nth-child(even){{background-color: #f2f2f2}}
                ''')

            print(f'Style is updated to {style}')

    # memento pattern for undo and redo
    def undo(self):
        if len(self._history) > 0:
            self._commands[self._history.pop()].undo()
            print('Undo is done')
        else:
            print('Undo is not possible')

    def redo(self):
        if len(self._history) > 0:
            self._commands[self._history[-1]].execute()

    
    @property
    def history(self):
        return self._history

    @property
    def commands(self):
        return self._commands


# main
if __name__ == '__main__':
    #create_html_page(default_settings)
    # create database
    conn = new_conn('CommandWebPage/database.db')
    # create controller
    controller = Controller()
    # create receiver
    table = Table()

    # # create commands
    add_style = NewStyle(table, {'font_size': fakeD.random_int(
        min=8, max=38), 'font_color': fakeD.color(), 'font_weight': 500, 'background_color': fakeD.color()})
    default_style = DefaultStyle(table)
    update_style = UpdateStyle(table)
    # # #add commands to controller
    controller.add_command('add_style', add_style)
    controller.add_command('default_style', default_style)

    # #execute commands
    # #
    controller.execute_command('add_style')
    controller.update_style()
    #bug1
    #controller.execute_command('default_style')
    # #undo commands
    controller.execute_command('add_style')
    
    controller.undo()
    controller.update_style()

    # controller.redo()

    # #close database
    # controller.close()
