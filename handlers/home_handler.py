import webapp2
from common import template


class HomeHandler(webapp2.RequestHandler):
    def get(self):
        View = template.Jinja("templates/pages/home")
        self.response.out.write(View.render())

    def post(self):
        pass
