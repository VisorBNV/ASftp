#!/usr/bin/python3

from ASftp import ASftp
import json

srv = ASftp('http://localhost:5000', 'admin', 'secret')
result = srv.test_connection()
print('Server: ', srv.ServerURL)
print('User: ', srv.srv_user, ', Password: ', srv.srv_pass, ', Auth-hash: ', srv.auth)
print('Connected: ', result)
print('Endpoint: ', srv.get_data('ftp_data').json()['_links']['self']['title'])
new_data = dict(data1="", data2="")
new_data['data1'] = input('what to put into ftp_data?:')
print('will post:', new_data)
answer = input('really?(y/n)')
if answer =='n':
    print('canceled!')
else:
    result = srv.post_data('ftp_data', new_data)
    if result.status_code != 201:
        print('Error!!! Code:', result.status_code)
        print(result.text)
    else:
        print(result.json())
        print('Saccesfull!')
print('Communication session closed.')
