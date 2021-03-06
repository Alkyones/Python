import sys,os
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QTableWidgetItem, QDialog
from PyQt5 import uic



import mysql.connector


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)

db = mysql.connector.connect( host="localhost", user="root", passwd="root", database="passwords")
cursor = db.cursor()
log_user = None

class PassHolder(QMainWindow):#
    

    def __init__(self):
        super().__init__()
        uic.loadUi(f'{BASE_DIR}\\UIs\\loginscreenUI.ui', self)
        print(f'{BASE_DIR}\\UIs\\showscreenUI.ui')
        self.setWindowTitle('PassHolder')
        

        self.password_input.setEchoMode(2)
        self.login_button.clicked.connect(self.login)
        self.signup_button.clicked.connect(self.register)


    def login(self):
            
        log_username = self.username_input.text()
        log_user = log_username
        password = self.password_input.text()
        if log_username == '' or password == '':
            self.error_message.setText('Please fill in all fields')
        else:
            cursor.execute("SELECT * FROM users WHERE username = '{}' AND password = '{}'".format(log_username, password))
            if cursor.fetchone() is None:
                self.error_message.setText('Username or password is incorrect')
            else:
                widget.setCurrentWidget(main)
                

                
       

    def register(self):
        self.error_message.setText('')

        widget.setCurrentWidget(register)

class RegisterScreen(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(f'{BASE_DIR}\\UIs\\registerscreenUI.ui', self)
        self.setWindowTitle('PassHolder')

        self.password_input.setEchoMode(2)
        
        self.register_button.clicked.connect(self.register)
        self.back_button.clicked.connect(self.back)

    def register(self):

        username = self.username_input.text()
        password = self.password_input.text()
        email = self.email_input.text()
        if username == '' or password == '' or email == '':
            self.error_message.setText('Please fill in all fields')
        else:
            cursor.execute(f"INSERT INTO users (Username, Password, Email) VALUES ('{username}', '{password}', '{email}')")
            db.commit()

            self.username_input.setText(''),self.password_input.setText(''),self.email_input.setText('')
            self.error_message.setText('Successfully registered')

    def back(self):
        widget.setCurrentWidget(window)


class MainScreen(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(f'{BASE_DIR}\\UIs\\mainscreenUI.ui', self)
        self.setWindowTitle('PassHolder')
        
        self.welcomeLabel.setText('Welcome back')

        log_user = 'root'

        self.showpassword_button.clicked.connect(self.show)
        self.addpassword_button.clicked.connect(self.add)

        self.back_button.clicked.connect(self.back)

    def show(self):
        widget.setCurrentWidget(show)

    def add(self):
        widget.setCurrentWidget(add)
    
    def back(self):
        widget.setCurrentWidget(window)


class AddPasswordScreen(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(f'{BASE_DIR}\\UIs\\addscreenUI.ui', self)
        self.setWindowTitle('PassHolder')
        
        self.add_button.clicked.connect(self.add)
        self.back_button.clicked.connect(self.back)

    def add(self):
        username = self.username_input.text()
        password = self.password_input.text()
        website = self.website_input.text()
        if username == '' or password == '' or website == '':
            self.error_message.setText('Please fill in all fields')
        else:
            cursor.execute(f"INSERT INTO passwords (Username, Password, Website,reg_user) VALUES ('{username}', '{password}', '{website}', '{log_user}')")
            db.commit()

            self.username_input.setText(''),self.password_input.setText(''),self.website_input.setText('')
            self.error_message.setStyleSheet('color: green')
            self.error_message.setText('Successfully added')

    def back(self):
        self.error_message.setStyleSheet('color: red')
        self.error_message.setText('')

        widget.setCurrentWidget(main)

class ShowPasswordScreen(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(f'{BASE_DIR}\\UIs\\showscreenUI.ui', self)
        self.setWindowTitle('PassHolder')
        
        self.back_button.clicked.connect(self.back)
    
        passwords = cursor.execute("SELECT Username,Password,Website FROM passwords WHERE reg_user = '{}'".format(log_user))
        print("SELECT Username,Password,Website FROM passwords WHERE reg_user = '{}'".format(log_user))
        passwords = cursor.fetchall()
        self.tableWidget.setRowCount(len(passwords))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(['Username', 'Password', 'Website'])
        for i in range(len(passwords)):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(passwords[i][1]))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(passwords[i][2]))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(passwords[i][3]))




    def back(self):
        widget.setCurrentWidget(main)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PassHolder()

    widget = QStackedWidget()
    widget.addWidget(window)
    main,register,add,show = MainScreen(), RegisterScreen(), AddPasswordScreen(), ShowPasswordScreen()
    widget.addWidget(main),widget.addWidget(register),widget.addWidget(add),widget.addWidget(show)



    widget.setFixedHeight(700)
    widget.setFixedWidth(700)

    widget.show()
    app.exec()