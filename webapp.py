from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)

@app.route("/")
def index():
    return "Flask App!"

@app.route("/plants")
def plants():
    return render_template('plants.html')

@app.route("/animals")
def animals():
    return render_template('animals.html')

@app.route("/humans")
def humans():
    return render_template('humans.html')

if __name__ == "__main__":
   app.run(host ='0.0.0.0', port = 5001, debug = True)
