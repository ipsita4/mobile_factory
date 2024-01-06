#test_app.py

import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_valid_order(self):
        # Test a valid order
        data = {
            "components": ["A", "D", "F", "I", "K"]
        }
        response = self.app.post('/orders', json=data)
        self.assertEqual(response.status_code, 201)


    def test_invalid_component(self):
        # Test an order with an invalid component
        data = {
            "components": ["A", "X", "D", "F", "I", "K"]
        }
        response = self.app.post('/orders', json=data)
        self.assertEqual(response.status_code, 400)

    def test_invalid_number_of_components(self):
        # Test an order with an invalid number of components in a category
        data = {
            "components": ["A", "D", "F", "I"]
        }
        response = self.app.post('/orders', json=data)
        self.assertEqual(response.status_code, 400)



if __name__ == '__main__':
    unittest.main()
