from flask import Flask, redirect, url_for, render_template, request, session, flash

app = Flask(__name__)

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

def runFlask():
    if __name__ == "__main__":
        app.run()

runFlask()