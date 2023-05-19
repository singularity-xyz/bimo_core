import datetime
from google.cloud import storage


class GCSClient:
    def __init__(self, bucket_name: str):
        self.client = storage.Client()
        self.bucket = self.client.get_bucket(bucket_name)

    def _get_blob(self, blob_name):
        """Creates a blob object."""
        blob = self.bucket.blob(blob_name)
        return blob

    def upload_blob(self, source_file_name, destination_blob_name):
        """Uploads a file to the bucket."""
        blob = self._get_blob(destination_blob_name)
        blob.upload_from_filename(source_file_name)

    def download_blob(self, blob_name, destination_file_name):
        """Downloads a blob from the bucket."""
        blob = self._get_blob(blob_name)
        blob.download_to_filename(destination_file_name)

    def list_blobs(self, prefix=None):
        """Lists all the blobs in the bucket."""
        blobs = self.bucket.list_blobs(prefix=prefix)
        return blobs

    def delete_blob(self, blob_name):
        """Deletes a blob from the bucket."""
        blob = self._get_blob(blob_name)
        blob.delete()

    def generate_signed_url(self, blob_name, expiration=3600):
        """Generates a signed URL for a blob."""
        blob = self._get_blob(blob_name)
        url = blob.generate_signed_url(datetime.timedelta(seconds=expiration))
        return url

    def get_blob_metadata(self, blob_name):
        """Get metadata of a blob."""
        blob = self._get_blob(blob_name)
        return blob.metadata

    def update_blob_metadata(self, blob_name, metadata):
        """Update metadata of a blob."""
        blob = self._get_blob(blob_name)
        blob.metadata = metadata
        blob.patch()

    def get_blob_info(self, blob_name):
        """Get all info of a blob."""
        blob = self._get_blob(blob_name)
        return blob._properties
