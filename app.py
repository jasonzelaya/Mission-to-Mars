# Dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
import pymongo
import os

# Establish connection
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

app = Flask(__name__)

# Create route that renders index.html template and finds documents from mongo
@app.route("/scrape")
def home():
    mars_info = mongo.db.mars_info.find_one()
