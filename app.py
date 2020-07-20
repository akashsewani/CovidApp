from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api
from pymongo import MongoClient
from bson.json_util import dumps

app = Flask(__name__)
api = Api(app)
conn = MongoClient()
db = conn.covidapp

@app.route('/api/v1/resources/dailycases/all', methods = ['GET'])
@app.route('/', methods=['GET'])

def DateWiseData_all():
    cursor = db.DailyCaseInfo.find({})
    list_cursor = list(cursor)
    json_data = dumps(list_cursor, indent=2)
    return render_template('base.html', contextlist=json_data)



@app.route('/allstates')
def StateWiseData_all():
    cursor = db.StatewiseCaseInfo.find({})
    list_cursor = list(cursor)
    json_data =dumps(list_cursor, indent=2)
    return json_data

@app.route('/state')
def StateWiseData():
    sc = request.args['sc']
    cursor = db.StatewiseCaseInfo.find({"statecode":sc})
    list_cursor = list(cursor)
    json_data =dumps(list_cursor, indent=2)
    return json_data

if __name__ == '__main__':
    app.run(debug=True) 
