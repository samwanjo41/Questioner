from flask import Blueprint, jsonify, make_response, request, flask
from app.api.v1.meetups-model import MeetupsModel

method1 = Blueprint('api', __name__,)
@method1.route('/api/vi/register', methods=['POST'])