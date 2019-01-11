from flask import Blueprint, jsonify, make_response, request
from ..models.question_model import QuestionsModel
from datetime import datetime
import re


question_view = QuestionsModel()

app1 = Blueprint('apiv3', __name__,)

@app1.route('/api/v1/question', methods=['POST'])
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

        