import re
import csv
import operator


def get_expenses_data(fields, filter_data, sort_items, order):
    
    expenses_data = []
    
    csvreader = read_file()
    data = filter(filter_data, csvreader)
    
    for row in data:
        data = get_data(fields, row)
        expenses_data.append(data)
    
    expenses_data = sort_data(expenses_data,sort_items,order)
    
    return expenses_data


def read_file():
    expenses_data = []
    with open("expenses.csv", 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            expenses_data.append(row)
    return expenses_data
    

def get_data(fields, row):
    if fields:
        data = {}
        if "departments" in fields: data["departments"] = row[0]
        if "project_name" in fields: data["project_name"] =row[1]
        if "amount" in fields: data["amount"] =row[2]
        if "date" in fields: data["date"] =row[3]
        if "member_name" in fields: data["member_name"] =row[4]
    else:
        data = {
            "departments" : row[0],
            "project_name" : row[1],
            "amount" : row[2],
            "date" : row[3],
            "member_name" : row[4]
        }
    return data


def filter(filter_data, data):
    
    if filter_data:
        if filter_data.get("departments"):
            data = [row for row in data if row[0]==filter_data.get("departments")]
        if filter_data.get("project_name"):
            data = [row for row in data if row[1]==filter_data.get("project_name")]
        if filter_data.get("amount"):
            data = [row for row in data if row[2]==filter_data.get("amount")]
        if filter_data.get("date"):
            data = [row for row in data if row[3]==filter_data.get("date")]
        if filter_data.get("member_name"):
            data = [row for row in data if row[4]==filter_data.get("member_name")]
            
    return data


def sort_data(data,sort_items,order):
    
    data = list(data)
    if sort_items:
        sort_items = sort_items.split(",")
    
    if sort_items:
        if order == 'desc':
            return sorted(data, key = lambda i: tuple([i[item] for item in sort_items]), reverse=True)
        data = sorted(data, key = lambda i: tuple([i[item] for item in sort_items]))
    
    return data


def aggregate_expenses(aggregate_option):
    expense_data = get_expenses_data(None, None, None, None)
    agregate_data = {}
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
    