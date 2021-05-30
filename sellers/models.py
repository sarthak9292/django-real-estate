from datetime import datetime
from django.db import models


class Seller(models.Model):
    name= models.CharField(max_length=200)
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    photo = models.ImageField(upload_to= 'photos/%Y/%m/%d/')
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name
