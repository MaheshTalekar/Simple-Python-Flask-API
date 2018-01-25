from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonify

db_connect = create_engine('sqlite:///Cars.db')
app = Flask(__name__)
api = Api(app)


class CAR(Resource):
    def get(self, car_id):
        conn = db_connect.connect()
        query = conn.execute("select make, model, year, car_id, last_updated, price from Cars where car_id =%d "  %int(car_id))
        result = {'car': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class CARLIST(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select make, model, year, car_id, last_updated, price from Cars;")
        result = {'car': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

    def post(self):
        conn = db_connect.connect()
        print(request.json)
        make = request.json['make']
        model = request.json['model']
        year = request.json['year']
        chassis_id = request.json['chassis_id']
        car_id = request.json['car_id']
        last_updated = request.json['last_updated']
        price = request.json['price']
        query = conn.execute("insert into Cars values('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(make, model, year, chassis_id, car_id, last_updated, price))
        return {'status':'success'}


api.add_resource(CAR, '/car/<car_id>')
api.add_resource(CARLIST, '/car')

if __name__ == '__main__':
     app.run()
