import mysql.connector


password = input('Enter your password: ')

try:
    # Connect to the database local and to admin
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=password,
        database="Passwords")
    cursor = mydb.cursor()

    #create the table if not existed
    cursor.execute("""CREATE TABLE IF NOT EXISTS Passwords (
    PassIndex INTEGER PRIMARY KEY AUTO_INCREMENT,
    Username VARCHAR(255),
    Password VARCHAR(255),
    Website VARCHAR(255))""")

    print('Connected to database')
except:
    print('Wrong password')
    exit()





def showPasswords():
    cursor.execute("SELECT * FROM Passwords")
    passwords = cursor.fetchall()
    for count in range(len(passwords)):
        print(f'{count+1}. {passwords[count][1]} - {passwords[count][2]} - {passwords[count][3]}') 
    print('\n')
          

def addPassword():
    user_name = input('Enter username: ')
    password = input('Enter password: ')
    website = input('Enter website: ')

    # Insert the data into the table
    cursor.execute(f"""INSERT INTO Passwords (Username, Password, Website)
    VALUES ('{user_name}', '{password}', '{website}')""")
    mydb.commit()

def changePassword(PassIndex):
    cursor.execute(f"""SELECT * FROM Passwords WHERE PassIndex = {PassIndex}""")
    passwords = cursor.fetchall()
    print(passwords)
    new_password = input('Enter new password: ')
    cursor.execute(f"""UPDATE Passwords SET Password = '{new_password}' WHERE PassIndex = {PassIndex}""")
    mydb.commit()



# Main loop
while True:

    print('\n1. Show passwords\n2. Add password\n3. Change password\n4. Exit\n')
    choice = input('Enter your choice: ')
    
    if choice == '1':
        showPasswords()
    elif choice == '2':
        addPassword()
    elif choice == '3':
        showPasswords()
        PassIndex = input('Enter the index of the password you want to change: ')
        changePassword(PassIndex)
    elif choice == '4':
        print('Goodbye')
        break
    else:
        print('Invalid Input')