import json
import unittest
from unittest.mock import patch
from io import BytesIO

from app import APIHandler


class TestAPIHandler(unittest.TestCase):

    def setUp(self):
        self.handler = APIHandler.__new__(APIHandler)
        self.handler.wfile = BytesIO()
        self.handler.headers = {}

    def test_health_endpoint(self):
        self.handler.path = "/health"

        with patch.object(self.handler, "send_response"), \
             patch.object(self.handler, "send_header"), \
             patch.object(self.handler, "end_headers"):
            self.handler.do_GET()

        response = json.loads(self.handler.wfile.getvalue())

        self.assertEqual(response["status"], "active")

    def test_post_empty_message(self):
        self.handler.path = "/messages"
        self.handler.headers = {"Content-Length": "2"}
        self.handler.rfile = BytesIO(b"{}")

        with patch.object(self.handler, "send_response"), \
             patch.object(self.handler, "send_header"), \
             patch.object(self.handler, "end_headers"):
            self.handler.do_POST()

        response = json.loads(self.handler.wfile.getvalue())

        self.assertEqual(response["error"], "message must not be empty")


if __name__ == "__main__":
    unittest.main()