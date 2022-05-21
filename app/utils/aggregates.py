import re
import csv
import operator
from app.utils.expenses import get_expenses_data


def get_aggregates(aggregate_option):
    expense_data = get_expenses_data(None, None, None, None)
    agregate_data = {}
    
    if aggregate_option and aggregate_option in {"departments", "project_name", "date", "member_name"}:
        for data in expense_data:
            value = data["amount"]
            value = re.sub("€","",value)
            value = re.sub(",","",value)
            if data[aggregate_option] in agregate_data:
                agregate_data[data[aggregate_option]] += float(value)
            else:
                agregate_data[data[aggregate_option]] = float(value)
        for key,value in agregate_data.items():
            value = f'{value}€'
            agregate_data[key] = value
            
    return agregate_data
    