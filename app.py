from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Assignment1(Resource):
    def get(self):
        return {'message': 'get request'}

    def post(self):
        data = request.get_json()
        content = {'a': data['a'],
                   'b': data['b'],
                   'hasil': data['a'] + data['b']
                   }
        return content


api.add_resource(Assignment1, '/')


if __name__ == '__main__':
    app.run()
