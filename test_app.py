import unittest
from app import app

class GreetTestCase(unittest.TestCase):
    def setUp(self):
        # Set up the test client
        self.app = app.test_client()
        self.app.testing = True  # Set testing mode to True

    def test_home(self):
        # Send a GET request to the '/' route
        response = self.app.get('/')
        
        # Check that the status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Check that the response data is the expected JSON
        self.assertEqual(response.get_json(), {"message": "Hello level 400 FET, Quality Assurance!"})

if __name__ == '__main__':
    unittest.main()
