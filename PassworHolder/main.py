import psycopg2

conn = psycopg2.connect(
    database='passwords_user',
    host='localhost',
    user='postgres',
    password='asdwer123',
    port=5432,    
)

cur = conn.cursor()


def create_password():
    website = input("Please enter the website : ")
    username = input("Enter the username : ")
    password = input("Enter the password : ")

    # try:
    cur.execute(f"INSERT INTO passwords(website, username, password) VALUES('{website}', '{username}', '{password}');")
    print("Password saved successfully!\n")
    # except:
        # print("Couldn't save password!")



def show_password():
    cur.execute(f"SELECT * FROM passwords")
    passwords = cur.fetchall()
    
    for i, password in enumerate(passwords, start=1):
        print(f'{i}-\t {password[1]}\t\t{password[2]}\t\t{password[3]}')
    print('\n')


def search_password():
    website = input("Please enter website name to search saved passwords : ")
    cur.execute(f"SELECT * FROM passwords WHERE website LIKE '%{website}%'")
    data = cur.fetchall()
    if not data:
        print("No saved passwords found")
    else:
         for i, password in enumerate(data, start=1):
            print(f'{i}-\t {password[1]}\t\t{password[2]}\t\t{password[3]}')
    print('\n')



while True:
    print("1-Save new password\n2-Show all saved passwords\n3-Search password\n4-Exit")
    desicion = input("Enter your desicion : ")
    conn.commit()


    if desicion == '1':
        create_password()
    elif desicion == '2':
        show_password()
    elif desicion == '3':
        search_password()
    elif desicion == '4':
        break
    else:
        print("invalid decision\n")

    


