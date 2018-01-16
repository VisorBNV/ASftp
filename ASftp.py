import requests
import json
import base64


class ASftp:


    def __init__(self, server_url):
        self.ServerURL = server_url

    def test_connection(self):
        try:
            r = requests.get(self.ServerURL)
            if r.status_code == 200:
                result = True
            else:
                result = False
        except:
            result = False
        return result

    def get_data(self, data_param, usrname, pwd):
        if usrname != '':
            ba = bytearray()
            ba.extend(map(ord, usrname+':'+pwd))
            auth = base64.b64encode(ba)
            hdr = {'Authorization': 'Basic '+auth.decode("utf-8")}
            print('Auth header: ', hdr)
            response = requests.get(self.ServerURL + '/' + data_param, headers=hdr)
        else:
            response = requests.get(self.ServerURL+'/'+data_param)
        return response.json()
