import json
import unittest 


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
        
          

    
    