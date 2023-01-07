from django.db import models




# Create your models here.
class Places(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    thumbnail_image = models.ImageField(upload_to='static/places')
    def __str__(self):
        return self.name
  
   