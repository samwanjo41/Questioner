
from flask import Blueprint, jsonify, make_response, request
from ..models.user_model import UsersModel
from app.api.v1.utils.validators import Validator



user_view = UsersModel()

v1 = Blueprint('api', __name__, url_prefix='/api/v1')


@v1.route('/register', methods=['POST'])
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

    if not Validator.check_name_format(firstname):
         return make_response(jsonify({'message':
                    'Invalid firstname format'}), 400)

    if not Validator.check_name_format(lastname):
         return make_response(jsonify({'message':
                    'Invalid lastname format'}), 400)
    
    if not Validator.check_username_format(username):
         return make_response(jsonify({'message':
                    'Invalid username format'}), 400)
    
    if not Validator.check_email_format(email):
         return make_response(jsonify({'message':
                    'Invalid email format'}), 400)
    
   
    if not Validator.check_password_strength(password):
         return make_response(jsonify({'message':
                    'Invalid password format'}), 400)

    response = user_view.create_user(firstname, lastname, othername, email, phonenumber, username, password)
    return make_response(jsonify({
            "Message": "User Created Successfully",
            "details": response,
            "status": 201
        }), 201)


@v1.route('/login', methods=['POST'])
def login():
    """This is the login method"""
    data = request.get_json()
    email = data['email']
    password = data['password']

    return make_response(jsonify({
        "status": "ok",
        "data": {
          "email": email,
         "password": password
        }
    }), 200)
