#!/usr/bin/python3

from ASftp import ASftp

srv = ASftp('http://localhost:5000')
result = srv.test_connection()
print('Server: ', srv.ServerURL)
print('Connected: ', result)
print(srv.get_data('ftp_action', 'admin', 'secret'))
