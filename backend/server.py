from flask import Flask
from flask_pymongo import PyMongo
import json
from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mc2"
mongo = PyMongo(app)

@app.route('/')
def hello():
    fakultet = mongo.db.fakulteti.find_one()
    return JSONEncoder().encode(fakultet)
    