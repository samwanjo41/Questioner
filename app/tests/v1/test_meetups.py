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
            "createdOn":"createdOn",
            "happeningOn": "happeningOn",
            "images": "images",            
            "location": "location",
            "tags": ["python", "Ihub"],
            "topic": "topic",
                     
        }

        self.meetup_data3 = {
            "meetup_date": "24 January 2018",
            "topic": "Machine learning",
            "about": " ",
            "location": "Nairobi, Kenya",
            "meetup_image": "ML.jpg"
        }     

      
    def test_upcoming_meetups(self):
        """user view upcoming meetups"""
        get_response = self.client.get('/meetups/upcoming', content_type='application/json')
        result = json.loads(get_response.data.decode())
        self.assertEqual(get_response.status_code, 200)
        self.assertEqual(result["status"], 200)
        self.assertEqual(result['data'][0]['location'], 'location')
        
       
       

    def test_specific_meetups(self):
        """user view specific meetup by id"""
        today = datetime.utcnow().isoformat()
        self.client.post('/meetups', data=json.dumps(self.meetup3), content_type='application/json')
        my_response = self.client.get('/meetups/1', content_type='application/json')
        res = json.loads(my_response.data.decode())
        self.assertEqual(my_response.status_code, 200)
        self.assertEqual(res['data'][0]['location'], 'location')
       
       
        

    def test_create_meetups(self):
        """ create meetups"""
        response = self.client.post('/meetups', data=json.dumps(self.meetup3), content_type='application/json')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(result["status"], 201)
        self.assertEqual(result["Message"], "Meetup Created Successfully")
        self.assertEqual(result['data']['images'], 'topic')

    
    def test_no_location(self):
        '''Test create meetups'''
        self.client.post('/api/v1/meetups',
                         data=json.dumps(self.meetup_data3), content_type='application/json')
        self.assertRaises(ValueError)


    def test_no_topic(self):
        '''Test create meetups'''
        self.client.post('/api/v1/meetups',
                         data=json.dumps(self.meetup_data3), content_type='application/json')
        self.assertRaises(ValueError)
       
    def test_no_image(self):
        '''Test create meetups'''
        self.client.post('/api/v1/meetups',
                         data=json.dumps(self.meetup_data3), content_type='application/json')
        
        self.assertRaises(ValueError)
        
