import webapp2
from common import cloudstorage
from common import template
from google.appengine.ext import blobstore
from google.appengine.api import images

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        View = template.Jinja("/templates/pages/home")
        self.response.out.write(View.render())

    def post(self):
        self.response.headers["x-goog-project-id"] = "530140140149"
        self.response.headers["x-goog-acl"] = 'public-read-write'
        cloudstorage.RetryParams(
                                initial_delay=0.2,
                                max_delay=5.0,
                                backoff_factor=2,
                                max_retry_period=15
                            )
        # file_to_write = self.request.get("file")
        filename = "/geak-trash/somefile.jpg"
        with cloudstorage.open(filename, 'w', content_type='image/jpeg', options={'x-goog-acl': 'public-read-write'}) as gcsfile:
            gcsfile.write(self.request.get("file"))
            gcsfile.close()

        ofile = cloudstorage.open(filename)
        self.response.headers["Content-Type"] = "image/jpeg"
        self.response.out.write(dir(ofile))
        self.response.out.write(ofile)
        ofile.close()