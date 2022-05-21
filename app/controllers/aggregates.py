from flask import Blueprint, request, jsonify
from app.utils.aggregates import get_aggregates


aggregates_bp = Blueprint(
    'aggregates_bp', __name__,
)

@aggregates_bp.route('/', methods=['GET'])
def get_aggregate_api():
    
    data = request.args
    aggregate_option = data.get('by')
    
    expenses_data = get_aggregates(aggregate_option)
    
    return expenses_data