import pymongo
import pandas as pd
import json

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATABASE_NAME = "aps"
COLLECTION_NAME = "sensor-data"
FILE_PATH = "/config/workspace/aps_failure_training_set1.csv"



if __name__=="__main__":
    df = pd.read_csv(FILE_PATH)
    print(df.shape)

    #Convert Records into JSON
    df.reset_index(drop=True, inplace=True)
    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    #batch insert for json records
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)