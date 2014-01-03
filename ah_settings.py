# !/usr/bin python
import os

app = {
    "path": os.path.dirname(__file__)
}

config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': '6bded0f4f0f5fd217ac1675c6b71873824a1206658031558bc65f63807aeaf2c0ca61f08b88477caccf6938e3dfdc779',
}

# if __name__ == "__main__":
#     print app.get("path")