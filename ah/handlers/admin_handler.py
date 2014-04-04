from common import session, template
from google.appengine.ext.webapp import blobstore_handlers


class AdminHandler(session.SessionRequestHandler):
    def get(self, **routes):
        self.response.out.write("Inside Admin")
