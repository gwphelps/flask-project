from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin

app = Flask(__name__)
api = Api(app)
cors = CORS(app)

class HelloFresco(Resource):
  def get(self):
    return {'message': 'Hello from Flask!'}


class Status(Resource):
    def get(self):
        return True


api.add_resource(HelloFresco, '/')
api.add_resource(Status, '/status')


if __name__ == '__main__':
    app.run()
