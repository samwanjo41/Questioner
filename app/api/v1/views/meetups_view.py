from flask import Blueprint, jsonify, make_response, request
from ..models.meetups_model import MeetupsModel
from datetime import datetime
import re


meetups_view = MeetupsModel()

version2 = Blueprint('apiv2', __name__,)


@version2.route('/api/v1/meetups', methods=['POST'])
def createMeetup():
    try:
            data = request.get_json()
            images = data["images"]
            createdOn = data["createdOn"]
            location = data["location"]
            topic = data["topic"]
            happeningOn = data["happeningOn"]
            tags = data["tags"]
    
    except Exception as e:
        return jsonify({
            "Error": "Invalid {} Key field".format(e)
        }), 400
    
    response = meetups_view.create_meetups(images, happeningOn, location, topic, tags)

    return make_response(jsonify({
            "Message": "Meetup Created Successfully",
            "data": response,
            "status": 201
        }), 201)

        
@version2.route('/api/v1/meetups/upcoming', methods=['GET'])
def get_meetups():
    """Get all meetups route."""
    meetups = MeetupsModel().get_all_meetups()
    return make_response(jsonify({
        "status": 200,
        "data": meetups
    }), 200)

    
@version2.route('/api/v1/meetups/<int:id>', methods=['GET'])
def get_specific_meetup(id):
    meetups = MeetupsModel().get_a_specific_meetup(id)
    return make_response(jsonify({
        "status": 200,
        "data": meetups
    }), 200)