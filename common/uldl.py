import ah_settings
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers


class UploadHandler(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        self.get_uploads("file")
        self.redirect()


class DownloadHandler(blobstore_handlers.BlobstoreDownloadHandler):
    def get(self, key):
        BlobKey = blobstore.BlobKey()
        Blob = blobstore.BlobInfo()