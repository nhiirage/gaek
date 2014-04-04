import ah_settings
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers


class UploadHandler(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        self.get_uploads("file")
        self.redirect()


class DownloadHandler(blobstore_handlers.BlobstoreDownloadHandler):
    def get(self, key):
        BlobKey = blobstore.BlobKey(key)
        Blob = blobstore.BlobInfo(BlobKey)
        self.send_blob(Blob, save_as='')

# BlobInfo
# filename, size, creation, content_type