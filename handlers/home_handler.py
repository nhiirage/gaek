import webapp2
from common import cloudstorage
from common import template
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers

# class GCSUploadHandler(blobstore_handlers.BlobstoreUploadHandler):
#     def post(self):


class HomeHandler(webapp2.RequestHandler):
    def get(self):
        View = template.Jinja("/templates/pages/home")
        self.response.out.write(View.render())

    def post(self):
        self.response.headers["x-goog-project-id"] = "530140140149"
        self.response.headers["x-goog-acl"] = "public-read-write"
        file_to_write = self.request.get("file")
        with cloudstorage.open('/geak-trash/20130314_142004.jpg', "w", "image/jpeg", options={'x-goog-acl': 'public-read-write'}) as gcsfile:
            gcsfile.write(file_to_write)
            gcsfile.close()

        self.response.out.write("Hello There!")