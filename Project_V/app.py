from flask import Flask, redirect, url_for, render_template, request, session, flash
from pymongo import MongoClient

app = Flask(__name__)

#mongo = MongoClient('')

#--Code Here--

@app.route('/')
def home():
    return render_template("pages/index.html")

@app.route('/about')
def vendor():
    return render_template("pages/about.html")

#-------------

if __name__ == "__main__":
    app.run()