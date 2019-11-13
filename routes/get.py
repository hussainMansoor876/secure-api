from flask import Blueprint, Flask, jsonify, request
from flask_pymongo import PyMongo
import os
from dotenv import load_dotenv
import json

load_dotenv()

app = Flask(__name__)
app.config['MONGO_DBNAME'] = os.getenv('MONGO_DBNAME') #connect the database
app.config['MONGO_URI'] = os.getenv('MONGO_URI')


get_blueprint = Blueprint('get', __name__)
mongo = PyMongo(app, retryWrites=False) #connect the database from flask app


@get_blueprint.route("/all")   # get all data from database
def all():
    vanilla = mongo.db.vanilla
    vanilla_data = vanilla.find({})
    data = []
    for x in vanilla_data:
        x['_id'] = str(x['_id'])
        data.append(x)
    return jsonify({'data': data})
