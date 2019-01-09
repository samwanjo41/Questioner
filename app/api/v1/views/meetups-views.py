from flask import Blueprint, jsonify, make_response, request, flask
from app.api.v1 import meetups-model
from app.api.v1.meetups-model import MeetupsModel


meetups-view = meetups-model.MeetupsModel()

method1 = Blueprint('api', __name__,)


@method1.route('/api/v1/register/meetups/upcoming', methods=['GET'])
def get_meetups():
    """Get all meetups route."""
    meetups = m.get_all()
    return jsonify({
        "status": 200,
        "data": meetups
    })