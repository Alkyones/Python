import os, sys
import json
from database import Database
credentialFile = os.path.abspath(os.path.join(
                                              os.path.dirname(os.path.realpath(__file__)),
                                              '../../credentials')
                                 )
def get_credentials():
    try:
        with open(f'{credentialFile}/amazonPipeline.json', 'r') as file:
            creds = json.load(file)
            file.close()
            return {"connectionUrl": creds['dbUrl'], "collectionName": creds['collectionName'], "dbName": creds['dbName']}
    except:
        print('Could not find credential file or credentials.')
        return None


credentials= get_credentials()
if credentials is None:
    print('No credentials found hence program is closed.')
    sys.exit("No credentials found hence program is closed.")

DB = Database(credentials)









DB.disconnectDb()