from flask import Blueprint, jsonify, make_response, request
from ..models.question_model import QuestionsModel
from datetime import datetime
import re
from app.api.v1.utils.validators import dataValidator


question_view = QuestionsModel()

v1 = Blueprint('apiv3', __name__, url_prefix='/api/v1')

@v1.route('/question', methods=['POST'])
def createQuestion():
    try:
            data = request.get_json()
            createdBy = data["createdBy"]
            meetup = data["meetup"]
            title = data["title"]
            body = data["body"]
            votes = data["votes"]
               
    except Exception as e:
        return jsonify({
            "Error": " {} Key field is missing".format(e)
        }), 400

    if check_for_empty_string(title):
        return make_response(jsonify({
            "Error": "title cannot be empty"
        }), 400)
    

    if check_for_empty_string(body):
        return make_response(jsonify({
            "Error": "body cannot be empty"
        }), 400)

    if not check_name_format(title):
        return make_response(jsonify({
            "Error": "Title has invalid format"
        }), 400)
    
    response = question_view.create_questions(createdBy, meetup, title, body, votes)

    return make_response(jsonify({
            "Message": "Question Created Successfully",
            "data": response,
            "status": 201
        }), 201)

