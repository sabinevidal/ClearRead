from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_assets import Environment

db = SQLAlchemy()

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")
    # assets = Environment()
    # assets.init_app(app)

    db.init_app(app)

    with app.app_context():
        from . import models
        # Import parts of our application
        from .assets import compile_static_assets
        # from .auth import auth
        from .exmple import exmple
        from .home import home

        # Register Blueprints
        # app.register_blueprint(auth.auth_bp)
        app.register_blueprint(exmple.exmple_bp)
        app.register_blueprint(home.home_bp)

        # Compile static assets
        # compile_static_assets(assets)  # Execute logic
        # db.drop_all()
        db.create_all()

        return app

