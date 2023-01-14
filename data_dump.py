import pymongo
import pandas as pd
import json
# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATA_FILE_PATH = "/config/workspace/Concrete_Data.csv"
DATABASE_NAME = 'Concrete_DB'
COLLECTION_NAME = 'Concrete_Collection'

if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"rows & columns : {df.shape}")

    # convert dataframe to json so that we can dump these record in MongoDB
    df.reset_index(drop = True,inplace = False)
    json_record = list(json.loads(df.T.to_json()).values())
    #print(json_record[0])
    
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)