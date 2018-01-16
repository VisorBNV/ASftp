#!/usr/bin/python3
from eve import Eve
from eve.auth import BasicAuth


class MyBasicAuth(BasicAuth):

    def check_auth(self, username, password, allowed_roles, resource, method):
        return username == 'admin' and password == 'secret'

schema_info = {
    'name': {
        'type': 'string',
    },
    'status' : {
        'type' : 'string',
    },
}

schema_data = {
    'data1': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 10,
        'required': True,
    },
    'data2': {
        'type': 'string',
        'minlength': 0,
        'maxlength': 10,
    },
}



my_settings = {
    'MONGO_HOST': 'localhost',
    'MONGO_PORT': 27017,
    'MONGO_DBNAME': 'as_ftp',
    'RESOURCE_METHODS' : ['GET', 'POST'],
    'ITEM_METHODS' : ['GET', 'PATCH', 'PUT', 'DELETE'],
    'DOMAIN': {
        'ftp_server_info': {
            'schema' : schema_info
        },
		'ftp_data': {
            'authentication': MyBasicAuth,
            'schema' : schema_data
        },
		'ftp_action': {
            'authentication': MyBasicAuth
        },
		'ASftp_data': {
            'authentication': MyBasicAuth
        }
    }
}


app = Eve(settings=my_settings)
if __name__ == '__main__':
    app.run('',5000)
