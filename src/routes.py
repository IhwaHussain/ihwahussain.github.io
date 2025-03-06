"""
Ihwa Website Service

This services implements the website for navigating Ihwa Hussain's portfolio
"""

from flask import jsonify

from flask import request, abort
from flask import current_app as app  # Import Flask application
from flask_restx import Resource, fields, reqparse

######################################################################
# GET INDEX
######################################################################
@app.route("/")
def index():
    """Root URL response"""
    return app.send_static_file("index.html")