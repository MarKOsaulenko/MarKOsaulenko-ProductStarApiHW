from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api()

#Твиты
twits = {1: {"name": "Mark", "post": "Hello!"},
           2: {"name": "Vova", "post": "ProductStar"}}

parser = reqparse.RequestParser()
parser.add_argument("name", type=str)
parser.add_argument("post", type=str)

class Main(Resource):
    def get(self, twit_id):
        if twit_id == 0:
            return twits
        else:
            return twits[twit_id]

    def delete(self, twit_id):
        del twits[twit_id]
        return twits

    def post(self, twit_id):
        twits[twit_id] = parser.parse_args()
        return twits

    def put(self, twit_id):
        twits[twit_id] = parser.parse_args()
        return twits

api.add_resource(Main, "/api/twits/<int:twit_id>") # Для строки <name>/ для id <int:twit_id>
api.init_app(app)


if __name__ == '__main__':
    app.run(debug=True, port=3000, host='127.0.0.1')
