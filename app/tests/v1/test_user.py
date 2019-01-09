from app import create_app
import json
import unittest 

class TestUsers(unittest.TestCase):

    def setUp(self):
        """Initialize app and define test variables."""
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.user.data = {
                    "id": 2,
                    "firstname": "Samuel",
                    "lastname": "Wanjohi",
                    "othername": "SamWan",
                    "email": "Sam@wan.com",
                    "phoneNumber": "0716217949",
                    "username": "samwan76",
                    "registered": "Date",
                    "isAdmin": False,
                    "password": "kjney789" 
        }


    def test_register(self):
        response = self.client.post('api/auth/v1/register',
                                    data=json.dumps(self.user_data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_login(self):
        response = self.client.post('api/auth/v1/login',
                                    data=json.dumps(self.user_data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)