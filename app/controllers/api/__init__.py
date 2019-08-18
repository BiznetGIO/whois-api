from flask import Blueprint
from flask_restful import Api
from .whois import Whois

api_blueprint = Blueprint("api", __name__, url_prefix="/api")
api = Api(api_blueprint)


api.add_resource(Whois, "/whois/")
