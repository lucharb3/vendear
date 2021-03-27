from flask import Flask, redirect, url_for, render_template, request, session, flash
from pymongo import MongoClient

app = Flask(__name__)

<<<<<<< HEAD
mongo = MongoClient('')
=======
mongo = MongoClient('secret')
>>>>>>> 0f98301b2b58790c1a3d5325256147d8ca573c11
db = mongo['Vendear']

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

<<<<<<< HEAD
def runFlask():
    if __name__ == "__main__":
        app.run()

runFlask()
=======
if __name__ == "__main__":
    app.run()
>>>>>>> 0f98301b2b58790c1a3d5325256147d8ca573c11
