from flask import Blueprint, jsonify, make_response, request, flask
from app.api.v1.user_model import UsersModel

method1 = Blueprint('api', __name__,)

@method1.route('/api/vi/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        firstname = data["First Name"]
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

    if not check_name_format(firstname):
        return make_response(jsonify({
            "Error": "firstname is invalid"
        }), 400)

    if not check_name_format(lastname):
        return make_response(jsonify({
            "Error": "lastname  is invalid"
        }), 400)

    if not check_name_format(othername):
        return make_response(jsonify({
            "Error": "othername is invalid"
        }), 400)
    
    if not check_name_format(email):
        return make_response(jsonify({
            "Error": "email is invalid"
        }), 400)

    if not check_name_format(username):
        return make_response(jsonify({
            "Error": "username is invalid"
        }), 400)
    
    if not check_name_format(phonenumber):
        return make_response(jsonify({
            "Error": "phonenumber is invalid"
        }), 400)
    
    if not check_name_format(password):
        return make_response(jsonify({
            "Error": "password is invalid"
        }), 400)





    if check_for_empty_string(lastname):
        return make_response(jsonify({
            "Error": "First name is invalid"
        }), 400)
    
    response = user_view.create_user(
        firstname, lastname, othername, email, phonenumber, username, password
    )
    return make_response(jsonify({
            "Message": "User Created Successfully",
            "details": response
        }), 201)
    