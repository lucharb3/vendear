from pymongo import MongoClient

mongo = MongoClient('')
db = mongo['Vendear']
col = db['Test']

def saveVendor(vendor):
    col.insert_one(vendor)



print('end')