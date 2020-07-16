from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

class DefaultApi(Resource):
    def get(self):
        return "Default Api Get Called"
    def post(self):
        data = request.get_json()
        return jsonify({'data': data})

api.add_resource(DefaultApi, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 
