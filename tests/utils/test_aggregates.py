import json
import unittest
from pathlib import Path
from app.app import create_app
from app.utils.aggregates import get_aggregates


class TripsContollerTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
           
           
    def test_get_aggregates_by_departments(self):
        aggregate_data = get_aggregates("departments")
        print(aggregate_data)
        assert aggregate_data == {
            'IT': '3400.0€', 
            'HR': '6521.0€', 
            'Sales': '39211.0€', 
            'Finance': '20335.0€'
            }
        
    
    def test_get_aggregates_by_member_name(self):
        aggregate_data = get_aggregates("member_name")
        print(aggregate_data)
        assert aggregate_data == {
            'Sam': '7979.0€', 
            'George': '20588.0€', 
            'Matt': '26596.0€', 
            'Jennifer': '2924.0€', 
            'Ann': '11380.0€'
            }
        
        
    def test_get_aggregates_by_dates(self):
        aggregate_data = get_aggregates("date")
        print(aggregate_data)
        assert aggregate_data == {
            '10/2/2021': '1200.0€', 
            '2/4/2021': '1400.0€', 
            '3/8/2021': '800.0€', 
            '5/10/2021': '1823.0€', 
            '5/23/2021': '2839.0€', 
            '3/2/2021': '210.0€', 
            '3/1/2021': '720.0€', 
            '11/5/2021': '929.0€', 
            '4/17/2021': '2237.0€', 
            '1/13/2021': '5807.0€', 
            '7/26/2021': '5233.0€', 
            '11/25/2021': '14703.0€', 
            '5/19/2021': '2204.0€', 
            '2/14/2021': '9027.0€', 
            '9/30/2021': '7811.0€', 
            '12/30/2021': '6561.0€', 
            '4/9/2021': '3336.0€', 
            '7/31/2021': '2627.0€'
            }
        
        
    def test_get_aggregates_by_departments(self):
        aggregate_data = get_aggregates("project_name")
        print(aggregate_data)
        assert aggregate_data == {
            'Gaama': '29627.0€', 
            'Mars-NS1': '3943.0€', 
            'Asterin': '21737.0€', 
            'AlphaDeo': '5076.0€', 
            'Alph-23': '9084.0€'
            }
        
    