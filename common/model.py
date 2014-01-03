from google.appengine.ext import ndb


class BaseModel(ndb.Model):
    date_created  = ndb.DateTimeProperty()
    date_modified = ndb.DateTimeProperty() 