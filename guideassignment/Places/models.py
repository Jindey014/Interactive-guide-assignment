from django.db import models
import os


def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % (instance.name, 'thumbnail', ext)
    return os.path.join('thumbnails', filename)


# Create your models here.
class Places(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    thumbnail_image = models.ImageField(
        upload_to=content_file_name, default='thumbnail_default.jpg')
