from flask import Blueprint, Flask, jsonify, request, Response
from flask_pymongo import PyMongo
import math
import os
from dotenv import load_dotenv
import json
from flask_cors import CORS, cross_origin
import datetime
from pymongo import ReturnDocument


load_dotenv()

app = Flask(__name__)
app.config['MONGO_DBNAME'] = os.getenv('MONGO_DBNAME')
app.config['MONGO_URI'] = os.getenv('MONGO_URI')


post_blueprint = Blueprint('post', __name__)
mongo = PyMongo(app, retryWrites=False, connect=True)


@post_blueprint.route("/data", methods=["POST"])
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
