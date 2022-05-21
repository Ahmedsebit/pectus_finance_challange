from flask import Blueprint, request, jsonify
from app.utils.aggregates import get_aggregates


aggregates_bp = Blueprint(
    'aggregates_bp', __name__,
)

@aggregates_bp.route('/', methods=['GET'])
def get_aggregate_api():
    """
    Example endpoint returning agggreggates
    This is using docstrings for specifications.
    ---
    parameters:
      - name: by
        in: query
        type: string
        required: false
    responses:
      200:
        description: A calculates aggregate
        examples:
          aggregates: {
              'IT': '3400.0€', 
              'HR': '6521.0€',
              'Sales': '39211.0€', 
              'Finance': '20335.0€'}
    """
    data = request.args
    aggregate_option = data.get('by')
    
    expenses_data = get_aggregates(aggregate_option)
    
    return expenses_data