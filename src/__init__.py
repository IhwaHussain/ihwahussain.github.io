"""
Package: src
Package for the app models and services
This module creates and configures the Flask App and sets up the logging
"""

import sys
import flask
import flask_restx


############################################################
# Initialize Flask Instance
############################################################
def create_app():
    """Initiative the application"""
    app = Flask(__name__)

    with app.app_context():
        from src import routes
        return app