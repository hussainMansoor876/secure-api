from flask import Flask, jsonify
from dotenv import load_dotenv


load_dotenv()

from flask_cors import CORS, cross_origin
from routes import get, post

app = Flask(__name__)


CORS(app, allow_headers = ["Content-Type", "Authorization", "Access-Control-Allow-Credentials"], supports_credentials=True)

app.register_blueprint(get.get_blueprint, url_prefix='/get')
app.register_blueprint(post.post_blueprint, url_prefix='/post')

@app.route('/')
def index():
    return jsonify({ "message" : "Wellcome To RESTFUL APIs"})





if __name__=="__main__":
    app.run(debug=True, port=8080)