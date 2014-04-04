import os
from common import cloudstorage as gcs
import webapp2

# Retry can help overcome transient urlfetch or GCS issues, such as timeouts.
my_default_retry_params = gcs.RetryParams(initial_delay=0.2,
                                          max_delay=5.0,
                                          backoff_factor=2,
                                          max_retry_period=15)
gcs.set_default_retry_params(my_default_retry_params)

BUCKET = '/gaek-trash'


class MainPage(webapp2.RequestHandler):
  def get(self):
    filename = BUCKET + '/demo-testfile'
    self.response.headers["x-goog-project-id"] = "530140140149"
    self.response.headers['x-goog-acl'] = 'public-read-write'
    self.response.headers['Content-Type'] = 'text/plain'
    self.tmp_filenames_to_clean_up = []

    self.create_file(filename)

    self.read_file(filename)

    # self.stat_file(filename)
    # self.response.write('\n\n')

    # self.create_files_for_list_bucket(BUCKET)
    # self.list_bucket(BUCKET)
    # self.response.write('\n\n')

    # self.list_bucket_directory_mode(BUCKET)
    # self.response.write('\n\n')

    # self.delete_files()

  def create_file(self, filename):
    self.response.write('Creating file %s\n' % filename)
    write_retry_params = gcs.RetryParams(backoff_factor=1.1)
    gcs_file = gcs.open(filename, 'w', content_type='text/plain', options={'x-goog-acl': 'public-read-write'}, retry_params=write_retry_params)
    gcs_file.write('abcde\n')
    gcs_file.write('f'*1024 + '\n')
    gcs_file.close()
    self.tmp_filenames_to_clean_up.append(filename)

  def read_file(self, filename):
    self.response.write('Truncated file content:\n')

    gcs_file = gcs.open(filename)
    self.response.write(gcs_file.readline())
    gcs_file.seek(-1024, os.SEEK_END)
    self.response.write(gcs_file.read())
    gcs_file.close()

  def stat_file(self, filename):
    self.response.write('File stat:\n')

    stat = gcs.stat(filename)
    self.response.write(repr(stat))

  def create_files_for_list_bucket(self, bucket):
    self.response.write('Creating more files for listbucket...\n')
    filenames = [bucket + n for n in ['/foo1', '/foo2', '/bar', '/bar/1',
                                      '/bar/2', '/boo/']]
    for f in filenames:
      self.create_file(f)
    self.tmp_filenames_to_clean_up.extend(filenames)

  def list_bucket(self, bucket):
    self.response.write('\nListbucket result:\n')

    page_size = 1
    stats = gcs.listbucket(bucket + '/foo', max_keys=page_size)
    while True:
      count = 0
      for stat in stats:
        count += 1
        self.response.write(repr(stat))
        self.response.write('\n')

      if count != page_size or count == 0:
        break
      stats = gcs.listbucket(bucket + '/foo', max_keys=page_size,
                             marker=stat.filename)

  def list_bucket_directory_mode(self, bucket):
    self.response.write('\nListbucket directory mode result:\n')
    for stat in gcs.listbucket(bucket + '/b', delimiter='/'):
      self.response.write('%r' % stat)
      self.response.write('\n')
      if stat.is_dir:
        for subdir_file in gcs.listbucket(stat.filename, delimiter='/'):
          self.response.write('  %r' % subdir_file)
          self.response.write('\n')

  def delete_files(self):
    self.response.write('Deleting files...\n')
    for filename in self.tmp_filenames_to_clean_up:
      try:
        gcs.delete(filename)
      except gcs.NotFoundError:
        pass


app = webapp2.WSGIApplication([('/', MainPage)],
                              debug=True)