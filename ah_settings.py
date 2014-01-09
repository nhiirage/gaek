# !/usr/bin python
import os

app = {
    "name": "My Default App",
    "path": os.path.dirname(__file__),
    "buckets": [
            "gaek-trash",
        ]
}

# Generated secret key using 
# hashlib.sha384("some_string".encode('ascii', 'xmlcharrefreplace')).hexdigest()
config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': '6bded0f4f0f5fd217ac1675c6b71873824a1206658031558bc65f63807aeaf2c0ca61f08b88477caccf6938e3dfdc779',
}

debug = True

enable_admin = True