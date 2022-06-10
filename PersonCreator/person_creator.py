import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'person',
)
cur = db.cursor()



def gender_checker():    
    while True:
        gender = input('enter your gender: ')
        if gender == 'male':
            return 'male'
        if gender == 'female':
            return 'female'
        else:
            print('invalid')

def name_checker():
    while True:
        name = input('enter your name: ')
        if name.isalpha() == True:
            return name
        else:
            print('Invalid input')

def job_checker():
    print('choose a job(1-teacher/2-student/3-doctor/4-worker)')
    while True:
        choose_desicion = int(input('enter your operation: '))
        if choose_desicion == 1:
            return 'teacher'
        elif choose_desicion == 2:
            return 'student'
        elif choose_desicion == 3:
            return 'doctor'
        elif choose_desicion == 4:
            return 'worker'
        else:
            print('Invalid option.Try again')

def salary_checker():
    print('salary checker')
    while True:
        salary_amount = input('enter your amount: ')
        if salary_amount.isnumeric():
            print('salary is: ',salary_amount + '$')
            return int(salary_amount)
        else:
            print('invalid')


