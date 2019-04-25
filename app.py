from flask import Flask
from flask_restful import Resource, Api
from pymongo import MongoClient
import json
import os
from flask import request, jsonify


app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client.cadastrodb
for doc in db.posts.find():
    return(doc)
    # print(doc)
# class records(Resource):

# @app.route('/')
# def get():
#     return("hello")
    # star = db.posts
    # for s in star.find():
    #     return jsonify(s)

# @app.route('/user', methods=['GET', 'POST', 'DELETE', 'PATCH'])
# def user():
#     if request.method == 'GET':
#         query = request.args
#         data = mongo.db.posts.find(query)
#         return jsonify(data), 200
#
#     data = request.get_json()
# if __name__ == '__main__':
#     app.run(debug=True)
