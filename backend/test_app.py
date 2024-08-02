# App Test Script

import unittest
from app import app

class FlaskTestCase(unittest.TestCase):
    def test_predict(self):
        tester = app.test_client(self)
        response = tester.post('/predict', json={'review': 'I loved this movie!'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('sentiment', response.get_json())

if __name__ == '__main__':
    unittest.main()
