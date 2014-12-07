from flask import Flask, jsonify, request, make_response
from flask.ext.httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()


app = Flask(__name__)
from app.products import products
from app.crawler import crawler


@auth.get_password
def get_password(username):
    if username == 'kesj':
        return 'kesj'
    return None


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)
