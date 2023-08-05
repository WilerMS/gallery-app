from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://mongo/exampledb'

mongo = PyMongo(app)

db = mongo.db