from flask import Blueprint, Flask, jsonify, request, Response
from flask_pymongo import PyMongo
import os
from dotenv import load_dotenv
import json
import bcrypt
from flask_cors import CORS, cross_origin
import datetime
from bson.json_util import ObjectId
import jwt
import cloudinary as Cloud
from cloudinary import uploader
from pymongo import ReturnDocument


load_dotenv()

app = Flask(__name__)
app.config['MONGO_DBNAME'] = os.getenv('MONGO_DBNAME')
app.config['MONGO_URI'] = os.getenv('MONGO_URI')


post_blueprint = Blueprint('post', __name__)
mongo = PyMongo(app, retryWrites=False, connect=True)


@post_blueprint.route("/image", methods=["POST"])
def imageUpdate():
    image = mongo.db.image
    data = request.form
    data = dict(data)
    data['_id'] = ObjectId(data['_id'])
    image_status = image.find_one_and_update({"_id": data['_id'], "uid": data['uid']}, {"$set": data}, return_document=ReturnDocument.AFTER)
    print(image_status)
    if image_status:
        return jsonify({'success': True, 'message': 'Successfully Updated'})
    return jsonify({'success': False, 'message': 'Cannot update Image Data'})