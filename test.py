import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="person"
)

cur = db.cursor()


for i in range (100):
    cur.execute("INSERT INTO people (name, salary) VALUES (%s, %s)", (f"name{i}", i))

db.commit()