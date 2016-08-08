"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask
from flask_restful import Api
from servicelib import routes as slroutes
from userservice import resources

app = Flask(__name__)
api = Api(app)

slroutes.register_resource(api, resources.User, "/api")

