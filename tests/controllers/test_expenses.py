import json
import unittest
from pathlib import Path
from app.app import create_app


class TripsContollerTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
           
    def test_get_expenses(self):
        response = self.client().get('/api/pectus_finance/expenses')
        self.assertEqual(308, response.status_code)
    
    
    