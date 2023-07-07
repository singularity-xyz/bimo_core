import os
import pytest
from bimo_core import GCSClient
from bimo_core import logging

# Replace with your actual test bucket name
TEST_BUCKET_NAME = 'momo-ai'

# A sample file to upload/download during testing
TEST_FILE = 'user-1/clas-151/syllabus.pdf'

@pytest.fixture(scope="module")
def gc_storage():
    return GCSClient(TEST_BUCKET_NAME)

# def test_upload_blob(gc_storage):
#     gc_storage.upload_blob(TEST_FILE, TEST_FILE)
#     assert any(blob.name == TEST_FILE for blob in gc_storage.list_blobs())

# def test_download_blob(gc_storage):
#     gc_storage.download_blob(TEST_FILE, 'downloaded_' + TEST_FILE)
#     assert os.path.exists('downloaded_' + TEST_FILE)
#     os.remove('downloaded_' + TEST_FILE)

def test_list_blobs(gc_storage):
    blobs = gc_storage.list_blobs()
    assert any(blob.name == TEST_FILE for blob in blobs)
    logging.info(blobs)

# def test_delete_blob(gc_storage):
#     gc_storage.delete_blob(TEST_FILE)
#     assert not any(blob.name == TEST_FILE for blob in gc_storage.list_blobs())

def test_generate_signed_url(gc_storage):
    url = gc_storage.generate_signed_url(TEST_FILE)
    assert url.startswith('https://')
    logging.info(url)
    print(url)

# def test_blob_metadata(gc_storage):
#     metadata = {'key1': 'value1'}
#     gc_storage.update_blob_metadata(TEST_FILE, metadata)
#     assert gc_storage.get_blob_metadata(TEST_FILE) == metadata
#     logging.info(metadata)

# def test_blob_info(gc_storage):
#     info = gc_storage.get_blob_info(TEST_FILE)
#     assert 'name' in info
#     assert info['name'] == TEST_FILE
#     logging.info(info)
