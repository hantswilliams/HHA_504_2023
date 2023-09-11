"""

In the context of Python packages, any directory that contains a file named __init__.py is 
considered a package, and the __init__.py file is run as the package's initialization code. 
This allows for organized module management, helping you keep related modules bundled together.

Initialization Code: Anything you include in the __init__.py file gets executed when 
the package (or one of the modules inside it) is imported. This is often used to run initialization 
code for the package or to set up variables, constants, or functions that are meant to be used 
as part of the package's  interface.

"""


from flask import Flask
from .config import Config
# from .extensions import db, login_manager
from .modules import main, about, data

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # # Initialize extensions
    # db.init_app(app)
    # login_manager.init_app(app)

    # Register blueprints (modules)
    app.register_blueprint(main.main)
    app.register_blueprint(about.main)
    app.register_blueprint(data.main)

    return app
