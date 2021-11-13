import unittest
import ip_api
import requests

class TestAPI(unittest.TestCase):

    def test_userIP(self):
        result = ip_api.userIP('0.0.0.0')
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()