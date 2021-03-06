import os

from urllib.parse import urljoin
from django.conf import settings
from django.core.files.storage import FileSystemStorage as FSStorage
from django.core.files.storage import get_storage_class
from storages.backends.s3boto3 import S3Boto3Storage


class FileSystemStorage(FSStorage):
    def __init__(self, *args, file_overwrite=False, custom_domain='http://localhost:9000', **kwargs):
        self.file_overwrite = file_overwrite
        self.custom_domain = custom_domain
        super().__init__(*args, **kwargs)

    def get_available_name(self, name, max_length=None):
        if self.file_overwrite and self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return super().get_available_name(name, max_length)

    def url(self, name):
        url = super().url(name)
        if self.custom_domain is None:
            return url
        return urljoin(self.custom_domain, url)


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
    custom_domain = settings.S3_CUSTOM_DOMAIN
    default_acl = 'public-read'
    file_overwrite = False


class PrivateMediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
    custom_domain = None
    default_acl = 'private'
    file_overwrite = False


private_media_storage = get_storage_class(settings.DEFAULT_PRIVATE_FILE_STORAGE)
