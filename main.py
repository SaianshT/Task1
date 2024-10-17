from flask import Flask
from flask import send_file
from flask_restful import Resource, Api
import random
import os


app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        a = random.choice(os.listdir('C:/Users/user/PycharmProjects/pythonProject/.venv/dishes'))

        #return('C:/Users/user/PycharmProjects/pythonProject/.venv/dishes/' + a)
        #os.startfile(a)
        return send_file('C:/Users/user/PycharmProjects/pythonProject/.venv/dishes/' + a)



api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True, port=8001)
