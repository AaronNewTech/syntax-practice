from flask import Flask, make_response
from flask_restful import Resource, Api
import requests

# setup function variables
app = Flask(__name__)
api = Api(app)

# decourator route method
# @app.route('/')
# def index():
#     return "<H1>Space X API Routes</H1>"

# resource route method
class Index(Resource):
    def get(self):
        html_content = "<H1>Space X API Routes</H1>"
        response = make_response(html_content)
        response.headers['Content-Type'] = 'text/html'
        return response

api.add_resource(Index, '/')


# @app.route('/launches', methods=['GET'])
# def get_launches():
#     response = requests.get('https://api.spacexdata.com/v3/launches')
#     launch_data = response.json()
#     return launch_data


class Launches(Resource):
    def get(self):
        response = requests.get('https://api.spacexdata.com/v3/launches')
        launch_data = response.json()
        return launch_data

api.add_resource(Launches, '/launches')


# @app.route('/launches/<int:flight_number>', methods=['GET'])
# def get_launches_by_id(flight_number):
#     response = requests.get(f'https://api.spacexdata.com/v3/launches/{flight_number}')
    
#     if response.status_code == 200:
#         flight_data = response.json()
#         return flight_data
#     else:
#         return make_response({'error': 'Flight not found'}, 404)


class FlightByNumber(Resource):
    def get(self, flight_number):
        response = requests.get(f'https://api.spacexdata.com/v3/launches/{flight_number}')

        if response.status_code == 200:
            flight_data = response.json()
            return flight_data
        else:
            return make_response({'error': 'Flight not found'}, 404)

api.add_resource(FlightByNumber, '/launches/<int:flight_number>')


if __name__ == '__main__':
    app.run(port=5555, debug=True)