from google.appengine.ext import ndb
from common import model


class PasswordProperty(ndb.StringProperty):
    def _validate(self, password):
        pass

    def _from_base_type(self, password):
        pass

    def _to_base_type(self, password):
        pass


class User(model.Model):
    username = ndb.StringProperty()
    password = ndb.StringProperty()