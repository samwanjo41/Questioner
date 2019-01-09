"""
The user Model

"""
from datetime import datetime

users_list = []

class UsersModel():

    def __init__(self):
        self.db = users_list

    def create_user(self, firstname, lastname, othername, email, phoneNumber, username, password):
       payload = {
        "id" = len(self.db)+1
        "firstname" = firstname,
        "lastname" = lastname,
        "othername" = othername,
        "email" = email,
        "phoneNumber" = phoneNumber,
        "username" = username,
        "password" = password,
        "registered" = datetime.now(),
        "isAdmin" = False

       }
    self.db.append(payload)
        return payload
        
    def get_user_by_username(self, username):
        single_user = [user for user in self.db if user['username'] == username]
        if single_user:
            return single_user
        else:
            return False
            
    def get_user_by_id(self, id):
        single_user = [user for user in self.db if user['id'] == id]
        if single_user:
            return single_user
        else:
            return False
       
        