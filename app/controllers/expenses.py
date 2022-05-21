from flask import Blueprint, request, jsonify
from app.utils.expenses import get_expenses_data, aggregate_expenses


expenses_bp = Blueprint(
    'expenses_bp', __name__,
)

@expenses_bp.route('/expanses_data', methods=['GET'])
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


@expenses_bp.route('/expanses_data/aggregate_expenses', methods=['GET'])
def get_aggregate_expenses_api():
    data = request.args
    aggregate_option = data.get('by')
    
    expenses_data = aggregate_expenses(aggregate_option)
    return expenses_data