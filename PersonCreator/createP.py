import mysql.connector
from PersonCreator.person_creator import name_checker, gender_checker, job_checker, salary_checker

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'person',
)
cur = db.cursor()
def create_person():
    person_dict = {}

    #name
    person_dict['name'] = name_checker()
    #gender
    person_dict['gender'] = gender_checker()
    #job
    person_dict['job'] = job_checker()
    #salary
    person_dict['salary'] = salary_checker()

    cur.execute(f"INSERT INTO people(name,gender,job,salary) VALUES ('{person_dict['name']}','{person_dict['gender']}','{person_dict['job']}',{person_dict['salary']})")
    db.commit()