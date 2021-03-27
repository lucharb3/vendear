from flask import Flask, redirect, url_for, render_template, request, session, flash
from pymongo import MongoClient

app = Flask(__name__)

mongo = MongoClient('mongodb+srv://MainClusterAccess:aFwfefqOdhf3HhE8@maincluster.r3ote.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = mongo['Vendear']

print('Lista')
for a in db.list_collection_names():
    print(a)

#--Code Here--

@app.route('/')
def homePage():
    return render_template("pages/index.html")

@app.route('/about')
def vendorPage():
    return render_template("pages/about.html")

@app.route('/verify')
def verifyPage():
    return render_template("pages/verify.html")

#-------------

if __name__ == "__main__":
    app.run()