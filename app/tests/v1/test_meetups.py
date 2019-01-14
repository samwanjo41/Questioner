import json
import unittest 
from datetime import datetime


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
            "createdOn": "createdOn",
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

       

      
    def test_upcoming_meetups(self):
        """user view upcoming meetups"""
        response = self.client.get('/api/v1/meetups/upcoming', data=json.dumps(self.record1), content_type='application/json')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["status"], 200)
       
       

    def test_specific_meetups(self):
        """user view specific meetup by id"""
        response = self.client.get('/api/v1/meetups/1', data=json.dumps(self.meetup), content_type='application/json')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["status"], 200)

    def test_create_meetups(self):
        """ create meetups"""
        response = self.client.post('/api/v1/meetups', data=json.dumps(self.meetup3), content_type='application/json')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(result["status"], 201)
        self.assertEqual(result["Message"], "Meetup Created Successfully")
