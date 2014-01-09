from common import session
from common import template


class AuthHandler(session.SessionRequestHandler):
    def get(self):
        self.response.out.write("GET Auth Handler")

    def post(self):
        self.response.out.write("POST Auth Handler")

