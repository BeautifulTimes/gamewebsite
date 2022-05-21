from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
points = 0
app = Flask(__name__)
api = Api(app)
CORS(app)

class Users(Resource):
    def get(self):
        global points
        points = points + 1
        return points , 200
    def post(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('name')
        args = parser.parse_args()  # parse arguments to dictionary
        print(args)
       
    pass

api.add_resource(Users, '/users')  # '/users' is our entry point
if __name__ == '__main__':
    print("running")
    app.run()  # run our Flask app