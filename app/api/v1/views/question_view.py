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

@v1.route('/question/<int:question_id>/downvote/', methods=["PATCH"])
def downvote(question_id):
    try:
            data = request.get_json()
           
            meetup = data["meetup"]
            title = data["title"]
            body = data["body"]
            votes = data["votes"]
               
    except Exception as e:
        return jsonify({
            "Error": "Invalid {} Key field".format(e)
        }), 400
        """Upvote method"""
    if question_view.downvote(question_id) == question_id:
        return jsonify({'status': 404, 'message': 'Question not found'}), 404    
    else:
        downvote = question_view.downvote(question_id)

  
    return jsonify({'status': 200, 'message': 'Question has been downvoted successfully', 'data': downvote}), 200

       

@v1.route('/question/<int:question_id>/upvote/', methods=["PATCH"])
def upvote(question_id):
    try:
            data = request.get_json()
           
            meetup = data["meetup"]
            title = data["title"]
            body = data["body"]
            votes = data["votes"]
               
    except Exception as e:
        return jsonify({
            "Error": "Invalid {} Key field".format(e)
        }), 400
    upvote = question_view.upvote(question_id)   
    if upvote:
        return jsonify({'status': 200, 'message': 'Question has been upvoted successfully', 'data': upvote}), 200   
    else:
         return make_response(jsonify({
             "status": 404, 
             "error": "Question not found"
             }), 404)

