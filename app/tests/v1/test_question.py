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

        self.question_missing = {
            "id": 1,
            "createdOn": "Date",
            "createdBy": 1,
            "meetup": 1,
            "title": "Food",
            "body": "",
            "votes": 0

        }
        self.que = {
             "meetup": "meetup",
            "title": "title",
            "body": "body",
            "votes": "votes"
        }

    def test_create_question(self):
        response = self.client.post('/api/v1/question', data=json.dumps(self.question3), content_type='application/json')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(result["status"], 201)
        self.assertEqual(result["Message"], "Question Created Successfully")
        
    def test_get_a_question(self):
        """Test if the we can get a specific meetup"""
        response = self.client.get('/api/v1/questions/1',
                                   content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_get_all_question(self):
        """Test if the we can get all question records"""
        response = self.client.get('/api/v1/questions/',
                                   content_type='application/json')
        self.assertEqual(response.status_code, 404)
          
    def test_question_post_with_missing_value(self):
        """Test if missing value will output an error"""
        question = {
            'body' : 'How will AI impart kenya in 2030'
        }
        response = self.client.post('/api/v1/questions',
                                    data=json.dumps(
                                        question),
                                    content_type='application/json')
        data = response.get_json()
        self.assertEqual(response.status_code, 404)
        

    
    def test_upvote(self):
        
        """
        Tests if the enpoint can implement an up-vote on a question
        """
        response=self.client.patch(
            '/api/v1/question/1/upvote',data=json.dumps(self.que),
            content_type="application/json")
        data=response.get_json()
        assert response.status_code==200
       
       
