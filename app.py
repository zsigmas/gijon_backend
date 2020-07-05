from flask import Flask
from flask_restful import Resource, Api

import logging
import json

logging.basicConfig(level=logging.DEBUG,
                    format="%(levelname)s:%(funcName)s:[%(asctime)s]: %(message)s",
                    datefmt="%H:%M:%S")
log = logging.getLogger(__name__)

app = Flask(__name__)
api = Api(app)


# Flask Definition

@app.route('/')
def hello_world():
    log.info('Serving')
    return 'Hello World!'

# API definition
class ShowMap(Resource):
    def get(self):
        with open('../external_data/barrios-urbanos.geojson') as f:
            data = json.load(f)
            return data

class test(Resource):
    def get(self, num):
        return num

api.add_resource(ShowMap, '/map')
api.add_resource(test, '/test/<int:num>')

if __name__ == '__main__':
    app.run()
