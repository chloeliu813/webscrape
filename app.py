
from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo

import scrape_mars

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    return(render_template("index.html"))

@app.route("/scrape")
def names():
    #connect with mongodb
    
    #use update function (only ever have 1 collection in the db)
    
    return jsonify(scrape_mars.mars_data())

    """Return a list of all passenger names"""
 

if __name__ == '__main__':
    app.run(debug=True)
