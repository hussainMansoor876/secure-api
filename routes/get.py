from flask import Blueprint, Flask, jsonify, request
from flask_pymongo import PyMongo
import os
from dotenv import load_dotenv
import json
# from bson.json_util import ObjectId

load_dotenv()

app = Flask(__name__)
app.config['MONGO_DBNAME'] = os.getenv('MONGO_DBNAME')
app.config['MONGO_URI'] = os.getenv('MONGO_URI')


get_blueprint = Blueprint('get', __name__)
mongo = PyMongo(app, retryWrites=False)


@get_blueprint.route("/all")
def all():
    vanilla = mongo.db.vanilla
    vanilla_data = article.find({})
    data = []
    for x in article_data:
        x['_id'] = str(x['_id'])
        data.append(x)
    return jsonify({'data': data})
