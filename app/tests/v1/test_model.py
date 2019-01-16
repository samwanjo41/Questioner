import json
import unittest 


class TestUsers(unittest.TestCase):

    def setUp(self):
        """Initialize app and define test variables."""
        from app import create_app

        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.myuser = {
                    
                    "firstName": "Samuel",
                    "lastName": "Wanjohi",
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

        self.user_data1 = {
            "firstname": " ",
            "lastname": "lastname",
            "email": "firstnamelastname@gmail.com",
            "password": "Password12345",
            "confirm_password": "Password12345",
            "imagefile": "image.png"
        }

    def test_register(self):
        response = self.client.post('/register',
                                    data=json.dumps(self.myuser),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_login(self):
        response = self.client.post('api/v1/login',
                                    data=json.dumps(self.data1),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_firstname(self):
        '''test for firstname'''
        self.client.post(
            '/api/v1/register',
            data=json.dumps(self.user_data1), content_type='application/json')
        self.assertRaises(ValueError)

    def test_lastname(self):
        '''Test for invalid firstname'''

        self.client.post(
            '/api/v1/auth/registration',
            data=json.dumps(self.user_data1), content_type='application/json')
        self.assertRaises(ValueError)

    def test_password(self):
        '''Test for password'''
        self.client.post(
            '/api/v1/auth/registration',
            data=json.dumps(self.user_data1), content_type='application/json')
        self.assertRaises(ValueError)

    def test_images(self):
        '''Test for image'''
        self.client.post(
            '/api/v1/auth/registration',
            data=json.dumps(self.user_data1), content_type='application/json')
        self.assertRaises(ValueError)


