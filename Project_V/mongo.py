from pymongo import MongoClient

mongo = MongoClient('')
db = mongo['Vendear']
vendors = db['Vendors']

def insertVendor(vendor):
    vendors.insert_one(vendor)



print('end')