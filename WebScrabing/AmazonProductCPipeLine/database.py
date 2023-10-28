from pymongo import MongoClient

class Database:
    def __init__(self, credentials):
        self.connection = self.connectDb(credentials)

    def connectDb(self, credentials):
        try:
            db = MongoClient(credentials['connectionUrl'])
            database = db[credentials['dbName']]
            print("Connected to Mongo")
            return database
        except Exception as e:
            print(f"Failed to connect to the database: {e}")
            return None

    def insertDoc(self, collection, doc):
        try:
            col = self.connection[collection]
            col.insert_one(doc)
            return True
        except Exception as e:
            print(f"Failed to insert document: {e}")
            return False

    def disconnectDb(self):
        try:
            if self.connection:
                self.connection.client.close()  # Close the MongoDB connection
                print("Disconnected from the database")
                return True
            else:
                print("No active database connection to disconnect.")
                return True  # Assuming this is a success in your application logic
        except Exception as e:
            print(f"Failed to disconnect from the database: {e}")
            return False