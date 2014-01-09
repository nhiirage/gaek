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
        file_to_write = self.request.get("file")
        with cloudstorage.open('/geak-trash/new_image', "w", "image/jpeg") as gcsfile:
            gcsfile.write(file_to_write)
        