from flask import Blueprint, Flask, jsonify, request, Response
from flask_pymongo import PyMongo
import math
import os
from dotenv import load_dotenv
import json


load_dotenv()

app = Flask(__name__)
app.config['MONGO_DBNAME'] = os.getenv('MONGO_DBNAME') #connect the database
app.config['MONGO_URI'] = os.getenv('MONGO_URI')


post_blueprint = Blueprint('post', __name__)
mongo = PyMongo(app, retryWrites=False, connect=True) #connect the database from flask app


@post_blueprint.route("/data", methods=["POST"]) #post request for adding the data
def index():
    vanilla = mongo.db.vanilla
    data = request.json
    timeRatio = 0
    if(data['time']['months']):
        timeRatio = data['time']['years'] + data['time']['months'] / 12
        print(timeRatio)
    vanillaCallOption = 0.4 * data['volatility'] * \
        math.sqrt(timeRatio) * data['basePrice']
    vanilla_data = {
        "volatility": data['volatility'],
        "timeRatio": timeRatio,
        "basePrice": data['basePrice'],
        "vanillaCallOption": vanillaCallOption
    }
    print(vanilla_data)
    vanilla.insert_one(vanilla_data)
    return jsonify({"success": True})
