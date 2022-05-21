from flask import Blueprint, request, jsonify
from app.utils.expenses import get_expenses_data


expenses_bp = Blueprint(
    'expenses_bp', __name__,
)

@expenses_bp.route('/', methods=['GET'])
def get_expanses_data_api():
    
    data = request.args
    fields = data.get('fields')
    filter_data = {
        "departments" : data.get('departments'),
        "project_name" : data.get('project_name'),
        "amount" : data.get('amount'),
        "date" : data.get('date'),
        "member_name" : data.get('member_name')
    }
    sort = data.get('sort')
    order = data.get('order')
    
    expenses_data = get_expenses_data(fields, filter_data, sort, order)
    
    return expenses_data
