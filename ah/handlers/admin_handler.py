import webapp2
from common import session, template


class AdminHandler(session.SessionRequestHandler):
    def get(self):
        V = template.Jinja("/ah/templates/pages/dashboard")
        self.response.out.write("Admin")