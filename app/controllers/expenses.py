from flask import Blueprint, request, jsonify
from app.utils.expenses import get_expenses_data


expenses_bp = Blueprint(
    'expenses_bp', __name__,
)

@expenses_bp.route('/', methods=['GET'])
def get_expanses_data_api():
    """
    Example endpoint returning expenses
    This is using docstrings for specifications.
    ---
    parameters:
      - name: fields
        in: query
        type: string
        required: false
      - name: departments
        in: query
        type: string
        required: false
      - name: project_name
        in: query
        type: string
        required: false
      - name: amount
        in: query
        type: string
        required: false
      - name: date
        in: query
        type: string
        required: false
      - name: member_name
        in: query
        type: string
        required: false
      - name: member_name
        in: query
        type: string
        required: false
      - name: sort
        in: query
        type: string
        required: false
      - name: order
        in: query
        type: string
        required: false
    
    responses:
      200:
        description: A calculates aggregate
        examples:
          rgb: []
    """
    
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
