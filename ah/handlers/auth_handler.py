from common import session
from common import template


class AuthHandler(session.SessionRequestHandler):
    def get(self):
        # View.template()
        pass

    def post(self):
        self.response.out.write("POST Auth Handler")

