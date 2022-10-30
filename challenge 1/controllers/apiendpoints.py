import json
from flask import  abort, request, Blueprint, jsonify, make_response
from modules import model as m
from flask_swagger_ui import get_swaggerui_blueprint

#defining my request api that will handle the requests and errors
REQUEST_API = Blueprint('request_api', __name__)
def get_blueprint():
    return REQUEST_API

#the api endpoint that will post new bids to the store and return sucess code of 200
@REQUEST_API.route('/bids', methods=['POST'])
def add_bid():
    if not request.get_json():
        abort(400)
    data = request.get_json()
    if not data.get('userid') :
        abort(400)
    if not data.get('petid'):
        abort(400)
    if not data.get('value'):
        abort(400)
    m.add_bid(data['petid'],data['value'],data['userid'])
    resp = {"status": "succeed"}
    resp_code = 200
    return json.dumps(resp),resp_code

#the api endpoint that will fetch all records in the bids table
@REQUEST_API.route('/bids', methods=['GET'])
def get_bids():
    output= m.get_bids()
    return output
#standard error handling
@REQUEST_API.errorhandler(400)
def handle_400_error(_error):
    """Return a http 400 error to client"""
    return make_response(jsonify({'error': 'Misunderstood'}), 400)

@REQUEST_API.errorhandler(401)
def handle_401_error(_error):
    """Return a http 401 error to client"""
    return make_response(jsonify({'error': 'Unauthorised'}), 401)


@REQUEST_API.errorhandler(404)
def handle_404_error(_error):
    """Return a http 404 error to client"""
    return make_response(jsonify({'error': 'Not found'}), 404)


@REQUEST_API.errorhandler(500)
def handle_500_error(_error):
    """Return a http 500 error to client"""
    return make_response(jsonify({'error': 'Server error'}), 500)


#this section is to define the swagger ui blueprint that will forward the schema to the server/swagger url
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.yml'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Just Bidding"
    }
)

def get_swagger():
    return SWAGGERUI_BLUEPRINT
