from flask import request
from flask_restful import Resource
from app.helpers.rest import response
from app.helpers import auth
import whois


class Whois(Resource):
    def post(self):
        headers = request.headers
        auth.load_dotenv()
        secret_key = auth.secret_key()
        request_key = headers.get("X-Whois-Key")

        if secret_key is None:
            return response(400, message=".whois.env not found")

        if request_key == secret_key:
            domain = request.data.decode()
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
