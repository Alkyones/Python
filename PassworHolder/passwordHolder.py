from pymongo import MongoClient




#connections
def discounnectDb(db):
    try:
        db.close()
        return True
    except:
        return False

def connectDb() :
    dbUrl = ''
    databaseName = ""
    db = MongoClient(dbUrl)
    database = db.PasswordHolder
    print("Connected to Mongo")
    return database

def connectCollection(dbQ):
    return dbQ.passwords
#insert  / remove

def insertPassword(): pass

def updatePassword(): pass

def removePassword(): pass

def listProgram(userDesicion="X"):
    print("Please select the action you want to perform...\n")
    print("1- Show saved passwords\n2- Search saved password\n3- Insert new password\n4- Update saved password\n5- Delete saved password")


db =  connectDb()
collection = connectCollection(db)


discounnectDb(db) 
