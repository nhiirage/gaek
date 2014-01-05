import webapp2
from common import session, template


class AdminHandler(session.SessionRequestHandler):
    def get(self, page=None):
        View = template.Jinja("/ah/templates/pages/dashboard")
        if page:
            self.response.out.write(page)
        else:
            self.response.out.write(page)