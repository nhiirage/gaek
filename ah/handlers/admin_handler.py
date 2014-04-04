from common import session, template
from google.appengine.ext.webapp import blobstore_handlers


class AdminHandler(session.SessionRequestHandler):
    def get(self, **routes):
        if not self.session.get('is_admin'):
            self.redirect('/ah/auth/')
        else:
            self.response.out.write(self.session.get('is_admin', 'Fuck!'))
