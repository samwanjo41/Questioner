import json
import unittest 

class TestUsers(unittest.TestCase):

    def setUp(self):
        """Initialize app and define test variables."""
        from app import create_app

        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.data = {
                    "id": 2,
                    "firstname": "Samuel",
                    "lastname": "Wanjohi",
                    "othername": "SamWan",
                    "email": "Sam@wan.com",
                    "phoneNumber": "0716217949",
                    "username": "samwan76",
                    "password": "kjney789" 
        }

        self.data1 ={
            'email': 'samwan@gmail.com',
            'username':'a12ngdggd'
        }


    def test_register(self):
        response = self.client.post('api/v1/register',
                                    data=json.dumps(self.data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_login(self):
        response = self.client.post('api/v1/login',
                                    data=json.dumps(self.data1),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)

class MeetupTest(unittest.TestCase):
    def setUp(self):
       from app import create_app

       self.app = create_app('testing')
       self.client = self.app.test_client()
       self.record1={
            'topic' : "AI",
            'location' : "iHub Upperhill,Nairobi Kenya " ,
            'happeningOn' : "Sat 14th Jan 2019",
        }
       self.record2 = {
            "meetup":"Ai",
            "topic":"using AI to create jobs",
            "status": "yes",
            "name":"alan"
        }
    
    def test_upcoming_meetups(self):
        """user view upcoming meetups"""
        response = self.client.get('/api/v1/meetups/upcoming', data= json.dumps(self.record1), content_type='application/json')
        self.assertEqual(response.status_code, 200)