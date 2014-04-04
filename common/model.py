from google.appengine.ext import ndb


class Model(ndb.Model):
    date_created  = ndb.DateTimeProperty(auto_now_add=True)
    date_modified = ndb.DateTimeProperty(auto_now=True) 