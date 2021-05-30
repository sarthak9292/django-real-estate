from django.db import models
from datetime import datetime
from sellers.models import Seller


class Listing(models.Model):
    seller = models.ForeignKey(Seller, on_delete= models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price= models.CharField(max_length=20)
    price_int = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    photo_main = models.ImageField(upload_to= 'photos/%Y/%m/%d/')
    photo_1 = models.ImageField(blank= True,upload_to= 'photos/%Y/%m/%d/')
    photo_2 = models.ImageField(blank= True,upload_to= 'photos/%Y/%m/%d/')
    photo_3 = models.ImageField(blank= True,upload_to= 'photos/%Y/%m/%d/')
    photo_4 = models.ImageField(blank= True,upload_to= 'photos/%Y/%m/%d/')
    photo_5 = models.ImageField(blank= True,upload_to= 'photos/%Y/%m/%d/')
    list_date= models.DateTimeField(default= datetime.now)
    is_published = models.BooleanField(default= True, blank=True)

    def __str__(self):
        return self.title

