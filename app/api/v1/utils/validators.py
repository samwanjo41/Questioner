"""Validation function to check app."""
import re
from app.api.v1.models import meetups_model
from datetime import datetime
class Validator():

    def check_empty_string(data):
        
        """
        Checks if data presented by a user is empty.
        """

        if data.strip() == "":
            return 'All fields are required'
        return None

    def check_date_format(date):

        """
        Check the date format.
        """
        if date != datetime.utcnow().isoformat():
            return 'Invalid date format'
        else:
            return True
        


    def check_number_format(number):
        """
        Check if value is a number.
        """
        if type(number) == int:
            return True
        return False


    def check_name_format(input_name):
        """
        Checks if name is 5 Characters and No integer allowed.
        """
        length_regex = re.compile(r'.{5,}')
        length = True if length_regex.search(input_name) is not None else False

        uppercase_regex = re.compile(r'[A-Z]')
        uppercase = True if uppercase_regex.search(
            input_name) is not None else False

        return(length and uppercase is True)


    def check_username_format(username):
        """
        Username should be 8 character long
        Contain special character
        Has an Integer and has a capitalize letter
        """
        length_regex = re.compile(r'.{8,}')
        length = True if length_regex.search(username) is not None else False

        uppercase_regex = re.compile(r'[A-Z]')
        uppercase = True if uppercase_regex.search(username) is not None else False

        special_char_regex = re.compile(r'[_@]')
        special_char = True if special_char_regex.search(
            username) is not None else False

        number_regex = re.compile(r'[0-9]')
        number = True if number_regex.search(username) is not None else False

        return(length and uppercase and special_char and number is True)


    def check_password_strength(password):
        """
        Password should be 8 character long
        Contain special character
        Has an Integer
        Has a capital letter
        """
        length_regex = re.compile(r'.{8,}')
        length = True if length_regex.search(password) is not None else False

        uppercase_regex = re.compile(r'[A-Z]')
        uppercase = True if uppercase_regex.search(password) is not None else False

        special_char_regex = re.compile(r'[_@]')
        special_char = True if special_char_regex.search(
            password) is not None else False

        number_regex = re.compile(r'[0-9]')
        number = True if number_regex.search(password) is not None else False
        return(length and uppercase and special_char and number is True)


    def check_email_format(email):
        """
        Should be email worthy.
        """
        if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]*\.*[com|org|edu]{3}$)",
                    email):
            res = True
        else:
            res = False
        return res

    def find_topic(topic):
        for each_meetup in meetups_model.meetups_rec:
            if each_meetup['topic'] == topic:
                return each_meetup