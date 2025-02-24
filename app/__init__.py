from flask import Flask
#from flask_babel import Babel

def create_app():
    """
    Creates the flask app instance, initializes the extensions (flask_login, flask_babel, flask_wtforms)
    and registers the blueprints.

    Args:
        config_class (custom Config class):

    Returns:
        flask app instance used for starting the server
    """

    app = Flask(__name__)
    #babel = Babel(app)
    #app.config['BABEL_DEFAULT_LOCALE'] = 'en'
    #app.config.from_object(config_class)

    from app.routes.home import bp as home_bp
    app.register_blueprint(home_bp)


    return app