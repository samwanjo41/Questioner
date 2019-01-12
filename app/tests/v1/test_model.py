import json
import unittest 


class TestUsers(unittest.TestCase):

    def setUp(self):
        """Initialize app and define test variables."""
        from app import create_app

        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.myuser = {
                    
                    "firstname": "Samuel",
                    "lastname": "Wanjohi",
                    "othername": "SamWan",
                    "email": "Sam@wan.com",
                    "phoneNumber": "0716217949",
                    "username": "samwan76",
                    "password": "kjney789" 
        }

        self.data1 = { 
            'email': 'samwan@gmail.com',
            'username': 'a12ngdggd'
        }

    def test_register(self):
        response = self.client.post('api/v1/register',
                                    data=json.dumps(self.myuser),
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
        self.record1 = {
            'topic': "AI",
            'location': "iHub Upperhill,Nairobi Kenya ",
            'happeningOn': "Sat 14th Jan 2019",
        }
        
        self.meetup = {
            "id": 1,
            "createdOn": "Date",
            "location": "Ihub",
            "topic": "Google I/O",
            "happeningOn": "Date",
            "Tags": ["python", "Ihub"],

        }

        self.meetup3 = {
            "images": "images",
            "createdOn": "createdOn",
            "location": "location",
            "topic": "topic",
            "happeningOn": "happeningOn",
            "tags": ["python", "Ihub"]
        }

        self.mitup = {
            "id": "id",
            "topic": "topic",
            "status": "status",
            "user": "username"
        }
        

      
    def test_upcoming_meetups(self):
        """user view upcoming meetups"""
        response = self.client.get('/api/v1/meetups/upcoming', data=json.dumps(self.record1), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_specific_meetups(self):
        """user view specific meetup by id"""
        response = self.client.get('/api/v1/meetups/1', data=json.dumps(self.meetup), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_create_meetups(self):
        """ create meetups"""
        response = self.client.post('/api/v1/meetups', data=json.dumps(self.meetup3), content_type='application/json')
        self.assertEqual(response.status_code, 201)

        """
    def test_rsvp_meetups(self):
        user rsvps upcoming meetups
        response = self.client.post('/api/v1/meetups/1/rsvp', data=json.dumps(self.mitup), content_type='application/json')
        self.assertEqual(response.status_code, 201) 
        """


class QuestionsTest(unittest.TestCase):
   
    def setUp(self):
        from app import create_app
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.question1 = {
            'user': 1,
            'meetup': 1,
            'title': "Entrance Ticket Price",
            'body':  "How much will be paid by each person for entrance"
        }
        self.question2 = {
            'user': 1,
            'meetup': 1,
            'title': "",
            'body':  "How much will be paid by each person for entrance"
        }

        self.question3 = {
            "createdBy": "createdBy",
            "meetup": "meetup",
            "title": "title",
            "body": "body",
            "votes": "votes"
        }

    def test_create_question(self):
        response = self.client.post('/api/v1/question', data=json.dumps(self.question3), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_get_all_question(self):
        response = self.client.post('/api/v1/question', data=json.dumps(self.question3), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    