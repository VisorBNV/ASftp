import requests
import json



class ASftp:


    def __init__(self,server_url):
        self.ServerURL = server_url

    def test_connection(self):
        try:
            requests.get(self.ServerURL)
            result = True
        except:
            result = False
        return result

    def get_data(self):
        response = requests.get(self.ServerURL)
        return response.json()
