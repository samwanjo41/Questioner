"""Test base class"""
import unittest
import json

from app import create_app


class BaseClassTest(unittest.TestCase):
    """This is the base class for test cases."""

    def setUp(self):
        """Initialize app and define test variables."""
        self.app = create_app('testing')
        self.client = self.app.test_client()

        self.admin_data = {
            "id": 1,
            "firstname": "Sam",
            "lastname": "Kiregi",
            "othername": "Samk234r",
            "email": "sam@kir.com",
            "phoneNumber": "0717654389",
            "username": "skirke",
            "registered": "Date",
            "isAdmin": True,
            "password": "kirsav45"
        }

        self.user_data = {
            "id": 2,
            "firstname": "Samuel",
            "lastname": "Wanjohi",
            "othername": "Samwan41",
            "email": "samwanjo41@gmail.com",
            "phoneNumber": "0716217949",
            "username": "samwanjo41",
            "registered": "Date",
            "isAdmin": False,
            "password": "Kujeni"
        }

        self.meetup = {
            "id": 1,
            "createdOn": "Date",
            "location": "Parklands",
            "topic": "IOT",
            "happeningOn": "Date",
            "Tags": ["IOT", "Parklands"],

        }

        self.question = {
            "id": 1,
            "createdOn": "Date",
            "createdBy": 1,
            "meetup": 1,
            "title": "Music",
            "body": "Jazz or Rhumba?",
            "votes": 1
        }

        self.rsvp = {
            "id": 1,
            "meetup": 1,
            "user": 1,
            "response": "Yes",
        }

    def log_in_user(self):
        """Create a user then log in the user"""
        self.client.post('/api/v1/auth/user/register',
                         data=json.dumps(self.user_data),
                         content_type='application/json')
        response = self.client.post('/api/v1/auth/user/login',
                                    data=json.dumps({
                                        "email": "samwanjo41@gmail.com",
                                        "password": "kujeni"
                                    }))
        return response 