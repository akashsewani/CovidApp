from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from pymongo import MongoClient
from bson.json_util import dumps


app = Flask(__name__)
api = Api(app)
conn = MongoClient()
db = conn.Bookstore
#or db = pymongo.MongoClient.Bookstore
db.Books.insert_one({"Name":"Book2"})
db.Books.insert_one({"Name":"Book3"})

cursor = db.Books.find({})
list_cursor = list(cursor)
json_data = dumps(list_cursor, indent=2)
print(json_data)


class DefaultApi(Resource):
    def get(self):
        return "Default Api Get Called"
    def post(self):
        data = request.get_json()
        return jsonify({'data': data})

api.add_resource(DefaultApi, '/')

if __name__ == '__main__':
    app.run(debug = True)

