import pytest

import whois
from app.helpers import common


class TestWhois:
    def fake_secret_key(self):
        return "fakekey123"

    def test_whois(self, client):
        common.secret_key = self.fake_secret_key
        # FIXME use fake
        # whois.query = self.fake_query

        data = "google.com"
        headers = {"X-Whois-Key": "fakekey123", "Content-Type": "text/plain"}

        res = client.post("/api/whois/", data=data, headers=headers)

        assert res.status_code == 200
        assert b"google.com" in res.data
