from flask import Blueprint, jsonify, make_response, request
from ..models.question_model import QuestionsModel
from datetime import datetime
import re


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
            "Error": "Invalid {} Key field".format(e)
        }), 400
    
    response = question_view.create_questions(createdBy, meetup, title, body, votes)

    return make_response(jsonify({
            "Message": "Question Created Successfully",
            "data": response,
            "status": 201
        }), 201)

   

@v1.route('/questions', methods=['GET'])
def get_questions():
    """Get all questions"""
    question = QuestionsModel().get_all_questions()
    if question:
        return make_response(jsonify({
        "status": 200,
        "data": question
    }), 200)
    else:
        return make_response(jsonify({
        "status": 404,
        "error": "No question created yet"
    }), 404)

@v1.route('/questions/<int:id>', methods=['GET'])
def get_a_question(id):
    """Get a specific question"""
    question = QuestionsModel().get_a_specific_question(id)
    if question:
        return make_response(jsonify({
        "status": 200,
        "data": question
    }), 200)
    else:
        return make_response(jsonify({
        "status": 404,
        "error": "No question created yet"
    }), 404)


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
    if not question_view.downvote(question_id):
        return jsonify({'status': 404, 'message': 'Question not found'}), 404    

    downvote = question_view.downvote(question_id, meetup, title, body, votes)

  
    return jsonify({'status': 200, 'message': 'Question has been upvoted successfully', 'data': downvote}), 200

       
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
        """Upvote method"""
    if not question_view.upvote(question_id):
        return jsonify({'status': 404, 'message': 'Question not found'}), 404    


    upvote = question_view.upvote(question_id)


  
    return jsonify({'status': 200, 'message': 'Question has been upvoted successfully', 'data': upvote}), 200

       