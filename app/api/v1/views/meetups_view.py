from flask import Blueprint, jsonify, make_response, request
from ..models.meetups_model import MeetupsModel
from datetime import datetime
import re


meetups_view = MeetupsModel()

v1 = Blueprint('apiv2', __name__, )


@v1.route('/meetups', methods=['POST'])
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
    response = meetups_view.create_meetups(images, happeningOn, location,
                                              topic, tags)

    return make_response(jsonify({
            "Message": "Meetup Created Successfully",
            "data": response,
            "status": 201
        }), 201)


@v1.route('/meetups/upcoming', methods=['GET'])
def get_meetups():
    """Get all meetups route."""
    meetups = MeetupsModel().get_all_meetups()
    if meetups:
        return make_response(jsonify({
        "status": 200,
        "data": meetups
    }), 200)
    else:
        return make_response(jsonify({
        "status": 404,
        "error": "No meetups created yet"
    }), 404)



@v1.route('/meetups/<int:id>', methods=['GET'])
def get_specific_meetup(id):
    meetups = MeetupsModel().get_a_specific_meetup(id)
    if meetups:
        return make_response(jsonify({
        "status": 200,
        "data": meetups
    }), 200) 
    else:
         return make_response(jsonify({
             "status": 404, 
             "error": "Meetup not found"
             }), 404)



@v1.route('/meetups/<int:id>/rsvp', methods=['POST'])
def rsvpMeetup(id):
    try:
            data = request.get_json()
            id = id
            topic = data['topic']  
            status = data['status']
            username = data['name']
    except Exception as e:
        return jsonify({
            "Error": "Invalid {} Key field".format(e)
        }), 400
    response = meetups_view.rsvp_for_meetup(id, topic, status,
                                              username)

    return make_response(jsonify({
            "Message": "Meetup Rsvp-ed Successfully",
            "data": response,
            "status": 201
        }), 201)
