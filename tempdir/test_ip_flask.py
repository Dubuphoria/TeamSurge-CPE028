import unittest
import ip_flask
import pytest
import requests
from flask import *

app = Flask(__name__)

class TestIndex(unittest.TestCase):

    def test_response(self):
        #===================================== FOR RESPONSE CODE
        test = app.test_client(self)
        url = "http://ipapi.co/0.0.0.0/json"
        Data = str(Response(url))
        self.assertEqual(Data.split(), ['<Response','28','bytes','[200','OK]>'])

    def test_IPADDRESSES(self):
        #===================================== IF FLASK IS COMMUNICATING AND RECEIVING DATA SHOULD BE TRUE
        test = app.test_client(self)
        url = "http://ipapi.co/0.0.0.0/json"
        parsed_info = requests.get(url)
        Data = parsed_info.json()
        ip_address = Data['ip']
        self.assertEqual(ip_address,"0.0.0.0")
        #===================================== IF ERROR ADDRESS IS PRIVATE SHOULD BE TRUE
        test = app.test_client(self)
        url = "http://ipapi.co/127.0.0.1/json"
        parsed_info = requests.get(url)
        Data = parsed_info.json()
        ip_address = Data['error']
        self.assertTrue(ip_address)
        #===================================== IF ERROR ADDRESS IS INVALID SHOULD BE TRUE
        test = app.test_client(self)
        url = "http://ipapi.co/wrong/json"
        parsed_info = requests.get(url)
        Data = parsed_info.json()
        ip_address = Data['error']
        self.assertTrue(ip_address)
    
    def test_IPv4ADD(self):
        #===================================== IF REGULAR ADDRESS IS INPUT SHOULD BE TRUE GETTING DATA REQUIRED
        test = app.test_client(self)
        url = "http://ipapi.co/175.176.17.203/json"
        parsed_info = requests.get(url)
        Data = parsed_info.json()
        ip_version = Data['version'] 
        ip_address = Data['ip']
        city = Data['city']
        latitude = Data['latitude']
        longitude = Data['longitude']
        timezone = Data['timezone']
        org = Data['org']
        asn = Data['asn']
        self.assertEqual(ip_address,"175.176.17.203")
        self.assertEqual(ip_version,"IPv4")
        self.assertEqual(city,"Quezon City")
        self.assertEqual(latitude,14.669)
        self.assertEqual(longitude,121.0438)
        self.assertEqual(timezone,"Asia/Manila")
        self.assertEqual(org,"Smart Broadband, Inc.")
        self.assertEqual(asn,"AS10139")

    def test_IPv6ADD(self):
        #===================================== IF REGULAR ADDRESS IS INPUT SHOULD BE TRUE GETTING DATA REQUIRED
        test = app.test_client(self)
        url = "http://ipapi.co/2001:4451:8221:6300:1cda:ea33:4f0f:2f04/json"
        parsed_info = requests.get(url)
        Data = parsed_info.json()
        ip_version = Data['version'] 
        ip_address = Data['ip']
        city = Data['city']
        latitude = Data['latitude']
        longitude = Data['longitude']
        timezone = Data['timezone']
        org = Data['org']
        asn = Data['asn']
        self.assertEqual(ip_address,"2001:4451:8221:6300:1cda:ea33:4f0f:2f04")
        self.assertEqual(ip_version,"IPv6")
        self.assertEqual(city,"Pasig")
        self.assertEqual(latitude,14.5783)
        self.assertEqual(longitude,121.0666)
        self.assertEqual(timezone,"Asia/Manila")
        self.assertEqual(org,"Philippine Long Distance Telephone Company")
        self.assertEqual(asn,"AS9299")

if __name__ == '__main__':
    unittest.main()