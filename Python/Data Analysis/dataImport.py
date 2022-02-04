from os import write
import os
import pandas as pd
from pymongo import MongoClient
import configparser
import json

# RUN ANOTHER PY FILE
exec(open('./init.py').read())

# IMPORT DATA USING MONGOIMPORT // MONGO DATATOOLS
def mongoimport(csv_path, db_name, coll_name, db_url='localhost', db_port=27000):
    """ Imports a csv file at path csv_name to a mongo colection
    returns: count of the documants in the new collection
    """
    client = MongoClient(db_url, db_port)
    db = client[db_name]
    coll = db[coll_name]
    data = pd.read_csv(csv_path)
    payload = json.loads(data.to_json(orient='records'))
    #coll.remove()
    coll.insert(payload)
    return coll.count()

# LIST ALL FILES IN FOLDER
def listAllFiles(mypath):
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    #print(len(onlyfiles))
    list = []
    for symbol in onlyfiles:
        #print(os.path.basename(symbol).split('.csv')[0])
        list.append(symbol)
    return list

# READ CONFIG FROM CONFIG.INI
config = configparser.ConfigParser()
config.read('./config.ini')
mypath = config['DEFAULT']['dataExport']
listSym = listAllFiles(mypath)
count = 0
for s in listSym:
    count = count + 1
    #print(s, round(100*count/len(listSym),2) , '%')
    collCount = mongoimport(mypath + s ,'dataAnalysis','Stock',config['DEFAULT']['host'],int(config['DEFAULT']['port']))
    print(collCount)
