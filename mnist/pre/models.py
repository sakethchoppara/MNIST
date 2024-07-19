from django.db import models
from uuid import uuid4 as u4

class Prediction(models.Model):
    image = models.ImageField(null=True,blank=True,upload_to='train/')
    id = models.UUIDField(primary_key=True,default=u4,editable=False)

# Create your models here.
