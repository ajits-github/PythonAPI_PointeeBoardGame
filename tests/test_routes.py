import unittest
from api.routes import app

class TestAPIRoutes(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_play_game_valid_rounds(self):
        response = self.client.open(method='GET', path='/play/25')
        self.assertEqual(response.status_code, 200, "Inside VALID rounds: Expected status code 200 but got {}".format(response.status_code))
        data = response.get_json()
        self.assertIn("coupon_values", data)
        self.assertIn("highest_value_coupons", data)

