import json
import requests

main_api = "http://ipapi.co/"
api_json = "/json"
api_json2 = "json"
keys_list = ["ip", "version", "city", "region", "latitude", "longitude", "timezone", "org"]

def userIP(ip_address):
    url = main_api + ip_address + api_json
    url_get = requests.get(url)
    return url_get
