import webapp2
from common import cloudstorage
from common import template
from google.appengine.ext import blobstore


class HomeHandler(webapp2.RequestHandler):
    def get(self):
        View = template.Jinja("/templates/pages/home")
        self.response.out.write(View.render())

    def post(self):
        self.response.headers["x-goog-project-id"] = "530140140149"
        self.response.headers["x-goog-acl"] = 'public-read-write'
        file_to_write = self.request.get("file")
        blobstore.create_gs_key("/gs/gaek-trash/somefile.jpg")
        with cloudstorage.open("/geak-trash/somefile.jpg", "w", "image/jpeg") as gcsfile:
            gcsfile.write(file_to_write)
        self.response.out.write("Hello There!")