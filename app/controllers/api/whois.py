from flask import request
from flask_restful import Resource

import whois
from app.helpers.rest import response
from app.helpers import common


class Whois(Resource):
    def post(self):
        headers = request.headers
        secret_key = common.secret_key()
        request_key = headers.get("X-Whois-Key")
        domain = request.data.decode()

        if secret_key is None:
            return response(400, message="secret key not found")

        if common.validate_domain(domain) is not True:
            return response(403, message="domain not supported")

        if request_key == secret_key:
            whois_data = whois.query(domain)
            data = {
                "name": whois_data.name,
                "registrar": whois_data.registrar,
                "creation_date": str(whois_data.creation_date),
                "expiration_date": str(whois_data.expiration_date),
                "last_updated": str(whois_data.last_updated),
                "name_servers": list(whois_data.name_servers),
            }
            return response(200, data=data)
        else:
            return response(401)
