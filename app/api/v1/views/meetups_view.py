from flask import Blueprint, jsonify, make_response, request
from ..models.meetups_model import MeetupsModel
from app.api.v1.utils.validators import Validator
from datetime import datetime
import re


meetups_view = MeetupsModel()

v1 = Blueprint('apiv2', __name__, )


@v1.route('/api/v1/meetups', methods=['POST'])
def createMeetup():
    try:
            data = request.get_json()
            images = data["images"]          
            location = data["location"]
            topic = data["topic"]
            happeningOn = data["happeningOn"]
            tags = data["tags"]
    except Exception as e:
        return jsonify({
            "Error": " {} Key field is missing".format(e)
        }), 400
    if not Validator.check_name_format(topic):
         
        return make_response(jsonify({'message':
                    'Invalid topic format'}), 400)

    if  Validator.check_empty_string(location):
         return make_response(jsonify({'message':
                    'Invalid location format'}), 400)
    
    if  Validator.check_empty_string(images):
         return make_response(jsonify({'message':
                    'Invalid images format'}), 400)
    
    if not Validator.check_date_format(happeningOn):
         return make_response(jsonify({'message':
                    'Invalid happeningOn format'}), 400)

    if  Validator.check_empty_string(tags):
         return make_response(jsonify({'message':
                    'Invalid tags format'}), 400) 
    
    meetup_found = MeetupsModel.get_meetup_by_topic(topic)
    venue_occupied = MeetupsModel.get_meetup_by_location(location)
    date_booked = MeetupsModel.get_meetup_by_date(happeningOn)

    response = meetups_view.create_meetups(images, happeningOn, location,
                                              topic, tags)
    
    if meetup_found is False:
        return make_response(jsonify({
                "Message": "Meetup Created Successfully",
                 "data": response,  
                "status": 201
            }), 201)

    else:
         return make_response(jsonify({
                "Message": "Topic already exists ",  
                          
                "status": 400
            }), 400)        


@v1.route('/api/v1/meetups/upcoming', methods=['GET'])
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




@v1.route('/api/v1/meetups/<int:id>', methods=['GET'])
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



@v1.route('/api/v1/meetups/<int:id>/rsvp', methods=['POST'])
def rsvpMeetup(id):
    try:
            data = request.get_json()
            topic = data['topic']  
            status = data['status']
            username = data['username']
         
    except Exception as e:
        return jsonify({
            "Error": "Invalid {} Key field".format(e)
        }), 400

    if Validator.check_empty_string(topic):
         return make_response(jsonify({'message':
                    'Invalid topic format'}), 400)

    if Validator.check_empty_string(status):
         return make_response(jsonify({'message':
                    'Invalid status format'}), 400)

    response = meetups_view.rsvp_for_meetup(id, topic, status, username)
    if id == id:
        return make_response(jsonify({
            "Message": "Meetup Rsvp-ed Successfully",
            "data": response,
            "status": 201
        }), 201)
    else:
        return make_response(jsonify({
            "error": "Meetup does not seem to exist",
            "status": 404            
        }))
