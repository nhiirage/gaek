import webapp2


class HomeHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("Home Handler")