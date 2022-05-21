import logging
from config import app_config
from flask_api import FlaskAPI
from flask_swagger_ui import get_swaggerui_blueprint


# db = SQLAlchemy()
# migrate = Migrate(db)

### swagger specific ###
SWAGGER_URL = '/api/pectus/swagger'
API_URL = '/static/swagger.json'
URL_PREFIX_EXPENSES = '/api/pectus_finance/expenses'
URL_PREFIX_AGGREGATES = '/api/pectus_finance/aggregates'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "pectus"
    }
)

logger = logging.getLogger(__name__)


def create_app(config_name):
    '''
    Wraps the creation of a new Flask object, and returns it after it's loaded up
    with configuration settings using app.config and connected to the DB using
    '''

    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])

    app.app_context().push()
    log_level = logging.INFO
    app.logger.setLevel(log_level)

    import app.controllers.expenses as expenses
    import app.controllers.aggregates as aggregates


    app.register_blueprint(expenses.expenses_bp, url_prefix=URL_PREFIX_EXPENSES)
    app.register_blueprint(aggregates.aggregates_bp, url_prefix=URL_PREFIX_AGGREGATES)
    app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
    
    return app
