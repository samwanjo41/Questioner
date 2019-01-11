
from flask import Blueprint, jsonify, make_response, request
from ..models.user_model import UsersModel

user_view = UsersModel()

method1 = Blueprint('api', __name__,)

@method1.route('/api/v1/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        firstname = data["FirstName"]
        lastname = data["LastName"]
        othername = data["othername"]
        email = data["email"]
        phonenumber = data["phonenumber"]
        username = data["username"]
        password = data["password"]
    except Exception as e:
        return jsonify({
            "Error": "Invalid {} Key field".format(e)
        }), 400
    
    response = user_view.create_user(firstname, lastname, othername, email, phonenumber, username, password        
    )
    return make_response(jsonify({
            "Message": "User Created Successfully",
            "details": response,
            "status": 201
        }), 201)
    


@method1.route('/api/v1/login', methods=['POST'])
def login():
    """This is the login method"""
    data = request.get_json()
    username = data['username']
    email = data['email']

    return make_response(jsonify({
        "status": "ok",
        "data": {
         "username": username,
         "email": email
        }
    }), 200)
