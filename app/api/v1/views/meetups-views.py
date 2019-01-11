from flask import Blueprint, jsonify, make_response, request, flask
from app.api.v1 import meetups-model
from app.api.v1.meetups-model import MeetupsModel
import re, datetime


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


@method1.route('/api/v1/meetups/<int:id>', methods=['GET'])
def get_specific_meetup(meetups_id):






@method1.route('/api/v1/meetups', methods=['POST'])
def createMeetup():
    meetup = {'id' : len(meetups) + 1,
              'createdOn' : datetime.datetime.now().strftime("%Y-%m-%d %H"),
              'location' : request.json['location'],
              'topic' : request.json['topic'],
              'happeningOn' : request.json['happeningOn'],
              'Tags':request.json['Tags']}

    return jsonify({'status' : 201,
                    'data' : [meetup]
                    'Message': 'Successfully created a meetup'})