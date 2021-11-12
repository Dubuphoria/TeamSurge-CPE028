import unittest
import ip_api
import requests

class TestAPI(unittest.TestCase):

    def test_userIP(self):
        url = "http://ipapi.co/0.0.0.0/json"
        parsed_info = requests.get(url)
        self.assertTrue(parsed_info)

if __name__ == '__main__':
    unittest.main()