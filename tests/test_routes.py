import unittest
from api.routes import app

class TestAPIRoutes(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    
