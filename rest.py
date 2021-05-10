# Using flask to make an api
# import necessary libraries and functions
import json
from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from sqlalchemy import create_engine
import pandas as pd
import scripts as s
import os

# creating a Flask app
app = Flask(__name__)
# creating an API object
api = Api(app)
# Create the database engine
engine = create_engine('mysql+mysqlconnector://root:usuario123@localhost:3306/axldraex')


# making a class for a particular resource
# the get, post methods correspond to get and post requests
# they are automatically mapped by flask_restful.
# other methods include put, delete, etc.
class Hello(Resource):

    # corresponds to the GET request.
    # this function is called whenever there
    # is a GET request for this resource
    def get(self):
        query = """
        SELECT * 
        FROM draexvent;
        """
        df = pd.read_sql(query, engine)
        result = df.to_json(orient='records')
        parsed = json.loads(result)
        return parsed

    # Corresponds to POST request
    def post(self):
        data = request.get_json()  # status code
        return jsonify({'data': data}), 201


# another resource to calculate the square of a number
class Square(Resource):

    def get(self, num):
        return jsonify({'square': num ** 2})


# jason post resourse
class PostJson(Resource):

    def post(self):
        print(request.is_json)
        content = request.get_json()
        print(content)
        return content


# testing parameters
class BarAPI(Resource):
    def get(self):

        parser = reqparse.RequestParser()
        parser.add_argument('key1', type=str)
        parser.add_argument('key2', type=str)

        return parser.parse_args()


# load excel for new materials expo
class LoadNewMateExpo(Resource):
    def get(self):
        return s.MultiLoad()


# adding the defined resources along with their corresponding urls
api.add_resource(Hello, '/')
api.add_resource(Square, '/square/<int:num>')
api.add_resource(PostJson, '/postjason')
api.add_resource(BarAPI, '/bar')
api.add_resource(LoadNewMateExpo, '/LoadNewMateExpo')


# driver function
if __name__ == '__main__':
    app.run(debug=True)
