

import json
import unittest
from pathlib import Path
from app.app import create_app
from app.utils.expenses import read_file, get_expenses_data, get_data, filter, sort_data


class TripsContollerTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.data = read_file()
      
      
    def test_get_expenses_data(self):
        output = get_expenses_data(None, None, None, None)
        assert output == [
            {'departments': 'IT', 'project_name': 'Gaama', 'amount': '1,200.00€', 'date': '10/2/2021', 'member_name': 'Sam'}, 
            {'departments': 'IT', 'project_name': 'Mars-NS1', 'amount': '1,400.00€', 'date': '2/4/2021', 'member_name': 'Sam'}, 
            {'departments': 'IT', 'project_name': 'Asterin', 'amount': '800.00€', 'date': '3/8/2021', 'member_name': 'George'}, 
            {'departments': 'HR', 'project_name': 'Mars-NS1', 'amount': '1,823.00€', 'date': '5/10/2021', 'member_name': 'Sam'},
            {'departments': 'HR', 'project_name': 'AlphaDeo', 'amount': '2,839.00€', 'date': '5/23/2021', 'member_name': 'Matt'}, 
            {'departments': 'HR', 'project_name': 'Gaama', 'amount': '210.00€', 'date': '3/2/2021', 'member_name': 'Matt'}, 
            {'departments': 'HR', 'project_name': 'Mars-NS1', 'amount': '720.00€', 'date': '3/1/2021', 'member_name': 'Jennifer'}, 
            {'departments': 'HR', 'project_name': 'Alph-23', 'amount': '929.00€', 'date': '11/5/2021', 'member_name': 'Sam'}, 
            {'departments': 'Sales', 'project_name': 'AlphaDeo', 'amount': '2,237.00€', 'date': '4/17/2021', 'member_name': 'Ann'}, 
            {'departments': 'Sales', 'project_name': 'Asterin', 'amount': '5,807.00€', 'date': '1/13/2021', 'member_name': 'Ann'}, 
            {'departments': 'Sales', 'project_name': 'Asterin', 'amount': '5,233.00€', 'date': '7/26/2021', 'member_name': 'George'}, 
            {'departments': 'Sales', 'project_name': 'Gaama', 'amount': '9,175.00€', 'date': '11/25/2021', 'member_name': 'Matt'},
            {'departments': 'Sales', 'project_name': 'Alph-23', 'amount': '5,528.00€', 'date': '11/25/2021', 'member_name': 'George'}, 
            {'departments': 'Sales', 'project_name': 'Gaama', 'amount': '2,204.00€', 'date': '5/19/2021', 'member_name': 'Jennifer'}, 
            {'departments': 'Sales', 'project_name': 'Gaama', 'amount': '9,027.00€', 'date': '2/14/2021', 'member_name': 'George'}, 
            {'departments': 'Finance', 'project_name': 'Gaama', 'amount': '7,811.00€', 'date': '9/30/2021', 'member_name': 'Matt'}, 
            {'departments': 'Finance', 'project_name': 'Asterin', 'amount': '6,561.00€', 'date': '12/30/2021', 'member_name': 'Matt'}, 
            {'departments': 'Finance', 'project_name': 'Asterin', 'amount': '3,336.00€', 'date': '4/9/2021', 'member_name': 'Ann'}, 
            {'departments': 'Finance', 'project_name': 'Alph-23', 'amount': '2,627.00€', 'date': '7/31/2021', 'member_name': 'Sam'}
            ]


    def test_read_file(self):
        output = read_file()
        assert output == [
            ['IT', 'Gaama', '1,200.00€', '10/2/2021', 'Sam'], 
            ['IT', 'Mars-NS1', '1,400.00€', '2/4/2021', 'Sam'], 
            ['IT', 'Asterin', '800.00€', '3/8/2021', 'George'], 
            ['HR', 'Mars-NS1', '1,823.00€', '5/10/2021', 'Sam'], 
            ['HR', 'AlphaDeo', '2,839.00€', '5/23/2021', 'Matt'], 
            ['HR', 'Gaama', '210.00€', '3/2/2021', 'Matt'], 
            ['HR', 'Mars-NS1', '720.00€', '3/1/2021', 'Jennifer'], 
            ['HR', 'Alph-23', '929.00€', '11/5/2021', 'Sam'], 
            ['Sales', 'AlphaDeo', '2,237.00€', '4/17/2021', 'Ann'], 
            ['Sales', 'Asterin', '5,807.00€', '1/13/2021', 'Ann'], 
            ['Sales', 'Asterin', '5,233.00€', '7/26/2021', 'George'], 
            ['Sales', 'Gaama', '9,175.00€', '11/25/2021', 'Matt'], 
            ['Sales', 'Alph-23', '5,528.00€', '11/25/2021', 'George'], 
            ['Sales', 'Gaama', '2,204.00€', '5/19/2021', 'Jennifer'], 
            ['Sales', 'Gaama', '9,027.00€', '2/14/2021', 'George'], 
            ['Finance', 'Gaama', '7,811.00€', '9/30/2021', 'Matt'], 
            ['Finance', 'Asterin', '6,561.00€', '12/30/2021', 'Matt'], 
            ['Finance', 'Asterin', '3,336.00€', '4/9/2021', 'Ann'], 
            ['Finance', 'Alph-23', '2,627.00€', '7/31/2021', 'Sam']
            ]
        

    def test_get_data(self):
        row = ['Finance', 'Alph-23', '2,627.00€', '7/31/2021', 'Sam']
        fields = ["departments", "project_name", "amount", "date", "member_name"]
        output = get_data(fields, row)
        assert output == {
            'departments': 'Finance', 
            'project_name': 'Alph-23', 
            'amount': '2,627.00€', 
            'date': '7/31/2021', 
            'member_name': 'Sam'
            }
        
    
    def test_filter(self):
        filter_data = {"departments":"Finance"}
        output = list(filter(filter_data, self.data))
        assert output == [
            ['Finance', 'Gaama', '7,811.00€', '9/30/2021', 'Matt'], 
            ['Finance', 'Asterin', '6,561.00€', '12/30/2021', 'Matt'], 
            ['Finance', 'Asterin', '3,336.00€', '4/9/2021', 'Ann'], 
            ['Finance', 'Alph-23', '2,627.00€', '7/31/2021', 'Sam']
        ]
        
    def test_filter_member_name(self):
        filter_data = {"member_name":"Sam"}
        output = list(filter(filter_data, self.data))
        assert output == [['IT', 'Gaama', '1,200.00€', '10/2/2021', 'Sam'], 
                          ['IT', 'Mars-NS1', '1,400.00€', '2/4/2021', 'Sam'], 
                          ['HR', 'Mars-NS1', '1,823.00€', '5/10/2021', 'Sam'], 
                          ['HR', 'Alph-23', '929.00€', '11/5/2021', 'Sam'], 
                          ['Finance', 'Alph-23', '2,627.00€', '7/31/2021', 'Sam']]
        
    def test_filter_project_name(self):
        filter_data = {"project_name":"Alph-23"}
        output = list(filter(filter_data, self.data))
        assert output == [
            ['HR', 'Alph-23', '929.00€', '11/5/2021', 'Sam'], 
            ['Sales', 'Alph-23', '5,528.00€', '11/25/2021', 'George'], 
            ['Finance', 'Alph-23', '2,627.00€', '7/31/2021', 'Sam']
        ]
        
        
        
    def test_filter_date(self):
        filter_data = {"date":"10/2/2021"}
        output = list(filter(filter_data, self.data))
        assert output == [['IT', 'Gaama', '1,200.00€', '10/2/2021', 'Sam']]
        
    
    def test_filter_amount(self):
        filter_data = {"amount":"1,200.00€"}
        output = list(filter(filter_data, self.data))
        assert output == [['IT', 'Gaama', '1,200.00€', '10/2/2021', 'Sam']]
        

    def test_sort_data(self):
        
        fields = ["departments", "project_name", "amount", "date", "member_name"]
        test_expenses = []
        data = filter(None, self.data)
        for row in data:
            data = get_data(fields, row)
            test_expenses.append(data)
        
        order = "desc"
        sort_items = 'departments,amount'
        output = sort_data(test_expenses,sort_items,order)
        assert output == [
            {'departments': 'Sales', 'project_name': 'Gaama', 'amount': '9,175.00€', 'date': '11/25/2021', 'member_name': 'Matt'}, 
            {'departments': 'Sales', 'project_name': 'Gaama', 'amount': '9,027.00€', 'date': '2/14/2021', 'member_name': 'George'}, 
            {'departments': 'Sales', 'project_name': 'Asterin', 'amount': '5,807.00€', 'date': '1/13/2021', 'member_name': 'Ann'}, 
            {'departments': 'Sales', 'project_name': 'Alph-23', 'amount': '5,528.00€', 'date': '11/25/2021', 'member_name': 'George'}, 
            {'departments': 'Sales', 'project_name': 'Asterin', 'amount': '5,233.00€', 'date': '7/26/2021', 'member_name': 'George'}, 
            {'departments': 'Sales', 'project_name': 'AlphaDeo', 'amount': '2,237.00€', 'date': '4/17/2021', 'member_name': 'Ann'},
            {'departments': 'Sales', 'project_name': 'Gaama', 'amount': '2,204.00€', 'date': '5/19/2021', 'member_name': 'Jennifer'}, 
            {'departments': 'IT', 'project_name': 'Asterin', 'amount': '800.00€', 'date': '3/8/2021', 'member_name': 'George'}, 
            {'departments': 'IT', 'project_name': 'Mars-NS1', 'amount': '1,400.00€', 'date': '2/4/2021', 'member_name': 'Sam'}, 
            {'departments': 'IT', 'project_name': 'Gaama', 'amount': '1,200.00€', 'date': '10/2/2021', 'member_name': 'Sam'}, 
            {'departments': 'HR', 'project_name': 'Alph-23', 'amount': '929.00€', 'date': '11/5/2021', 'member_name': 'Sam'}, 
            {'departments': 'HR', 'project_name': 'Mars-NS1', 'amount': '720.00€', 'date': '3/1/2021', 'member_name': 'Jennifer'}, 
            {'departments': 'HR', 'project_name': 'Gaama', 'amount': '210.00€', 'date': '3/2/2021', 'member_name': 'Matt'}, 
            {'departments': 'HR', 'project_name': 'AlphaDeo', 'amount': '2,839.00€', 'date': '5/23/2021', 'member_name': 'Matt'},
            {'departments': 'HR', 'project_name': 'Mars-NS1', 'amount': '1,823.00€', 'date': '5/10/2021', 'member_name': 'Sam'}, 
            {'departments': 'Finance', 'project_name': 'Gaama', 'amount': '7,811.00€', 'date': '9/30/2021', 'member_name': 'Matt'}, 
            {'departments': 'Finance', 'project_name': 'Asterin', 'amount': '6,561.00€', 'date': '12/30/2021', 'member_name': 'Matt'}, 
            {'departments': 'Finance', 'project_name': 'Asterin', 'amount': '3,336.00€', 'date': '4/9/2021', 'member_name': 'Ann'}, 
            {'departments': 'Finance', 'project_name': 'Alph-23', 'amount': '2,627.00€', 'date': '7/31/2021', 'member_name': 'Sam'}
            ]
        
    def test_sort_data_asc(self):
        
        fields = ["departments", "project_name", "amount", "date", "member_name"]
        test_expenses = []
        data = filter(None, self.data)
        for row in data:
            data = get_data(fields, row)
            test_expenses.append(data)
        
        order = "desc"
        sort_items = 'departments,amount'
        output = sort_data(test_expenses,sort_items,None)
        assert output == [
            {'departments': 'Finance', 'project_name': 'Alph-23', 'amount': '2,627.00€', 'date': '7/31/2021', 'member_name': 'Sam'}, 
            {'departments': 'Finance', 'project_name': 'Asterin', 'amount': '3,336.00€', 'date': '4/9/2021', 'member_name': 'Ann'}, 
            {'departments': 'Finance', 'project_name': 'Asterin', 'amount': '6,561.00€', 'date': '12/30/2021', 'member_name': 'Matt'}, 
            {'departments': 'Finance', 'project_name': 'Gaama', 'amount': '7,811.00€', 'date': '9/30/2021', 'member_name': 'Matt'}, 
            {'departments': 'HR', 'project_name': 'Mars-NS1', 'amount': '1,823.00€', 'date': '5/10/2021', 'member_name': 'Sam'}, 
            {'departments': 'HR', 'project_name': 'AlphaDeo', 'amount': '2,839.00€', 'date': '5/23/2021', 'member_name': 'Matt'}, 
            {'departments': 'HR', 'project_name': 'Gaama', 'amount': '210.00€', 'date': '3/2/2021', 'member_name': 'Matt'}, 
            {'departments': 'HR', 'project_name': 'Mars-NS1', 'amount': '720.00€', 'date': '3/1/2021', 'member_name': 'Jennifer'}, 
            {'departments': 'HR', 'project_name': 'Alph-23', 'amount': '929.00€', 'date': '11/5/2021', 'member_name': 'Sam'}, 
            {'departments': 'IT', 'project_name': 'Gaama', 'amount': '1,200.00€', 'date': '10/2/2021', 'member_name': 'Sam'}, 
            {'departments': 'IT', 'project_name': 'Mars-NS1', 'amount': '1,400.00€', 'date': '2/4/2021', 'member_name': 'Sam'}, 
            {'departments': 'IT', 'project_name': 'Asterin', 'amount': '800.00€', 'date': '3/8/2021', 'member_name': 'George'}, 
            {'departments': 'Sales', 'project_name': 'Gaama', 'amount': '2,204.00€', 'date': '5/19/2021', 'member_name': 'Jennifer'}, 
            {'departments': 'Sales', 'project_name': 'AlphaDeo', 'amount': '2,237.00€', 'date': '4/17/2021', 'member_name': 'Ann'}, 
            {'departments': 'Sales', 'project_name': 'Asterin', 'amount': '5,233.00€', 'date': '7/26/2021', 'member_name': 'George'}, 
            {'departments': 'Sales', 'project_name': 'Alph-23', 'amount': '5,528.00€', 'date': '11/25/2021', 'member_name': 'George'}, 
            {'departments': 'Sales', 'project_name': 'Asterin', 'amount': '5,807.00€', 'date': '1/13/2021', 'member_name': 'Ann'}, 
            {'departments': 'Sales', 'project_name': 'Gaama', 'amount': '9,027.00€', 'date': '2/14/2021', 'member_name': 'George'}, 
            {'departments': 'Sales', 'project_name': 'Gaama', 'amount': '9,175.00€', 'date': '11/25/2021', 'member_name': 'Matt'}
            ]