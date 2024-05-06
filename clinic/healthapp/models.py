from django.db import models

# Create your models here.
image = models.ImageField(upload_to="healthapp/images", default="")