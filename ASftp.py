import requests
import base64


class ASftp:


    def __init__(self, server_url, srv_user, srv_pass):
        self.ServerURL = server_url
        self.srv_user = srv_user
        self.srv_pass = srv_pass
        ba = bytearray()
        ba.extend(map(ord, self.srv_user + ':' + self.srv_pass))
        self.auth = base64.b64encode(ba)
        self.auth = self.auth.decode("utf-8")

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

    # получить данные с сервера в объекте Response (http://docs.python-requests.org/en/latest/api/#requests.Response)
    def get_data(self, endpoint):
        if self.srv_user != '':
            hdr = {'Authorization': 'Basic ' + self.auth, 'Content-Type': 'application/json'}
        else:
            hdr = {'Content-Type': 'application/json'}
        response = requests.get(self.ServerURL + '/' + endpoint, headers=hdr)
        return response

    # добавить(вставить) данные в базу на сервере. new_data = dict()
    def post_data(self, endpoint, new_data):
        if self.srv_user != '':
            hdr = {'Authorization': 'Basic ' + self.auth, 'Content-Type': 'application/json'}
        else:
            hdr = {'Content-Type': 'application/json'}
        response = requests.post(self.ServerURL + '/' + endpoint, json=new_data, headers=hdr)
        return response

    # изменить данные в базе на сервере. new_data = dict()
    def put_data(self, endpoint, new_data):
        if self.srv_user != '':
            hdr = {'Authorization': 'Basic ' + self.auth, 'Content-Type': 'application/json'}
        else:
            hdr = {'Content-Type': 'application/json'}
        response = requests.put(self.ServerURL + '/' + endpoint, json=new_data, headers=hdr)
        return response

