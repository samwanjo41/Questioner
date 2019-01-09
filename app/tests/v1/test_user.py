"""Test the user model file and views functionality"""
import json

from . import BaseClassTest



class TestUserModels(BaseClassTest):
    """Test case for the user model"""

   
    def test_signup(self):
        """"Test if a user can signup"""
        response = self.client.post('/api/v1/auth/user/register',
                                    data=json.dumps(self.user_data),
                                    content_type='application/json')
        result = json.loads(response.data.decode('UTF-8'))
        self.assertEqual(response.status_code, 201)
        self.assertTrue(result["message"], "Successfully registered")
        self.assertNotEqual(response.status_code, 404)

    def test_login(self):
        """Test if a registered user can login"""
        self.client.post('/api/v1/auth/user/register',
                         data=json.dumps(self.user_data),
                         content_type='application/json')
        response = self.client.post('/api/v1/auth/user/login',
                                    data=json.dumps({
                                        "email": "samwanjo41@gmail.com",
                                        "password": "Kujeni"
                                    }))

        result = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertTrue(result["message"], "Successfully logged in")