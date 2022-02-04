import configparser
import pymongo

config = configparser.ConfigParser()
config.read('./config.ini')
localhost = config['DEFAULT']['host']
localport = int(config['DEFAULT']['port'])
localdb = config['DEFAULT']['db']
localcol = config['DEFAULT']['col']

client = pymongo.MongoClient(host=localhost,port=localport)
db = client['dataAnalysis']
coll = db['Stock']
queryString = "{'Ticker':'ACB'}"
'''
for x in coll.find({},{"High":"34.7"}):
    print(x["Date"])
    '''
# use $regex to find docs that start with case-sensitive "obje"
query = { "Ticker": { "$regex": 'ACB*' } }
docs = coll.count_documents( query )
print ("query:", query)
print ("$regex using '.___*' -- total:", docs, "\n")

