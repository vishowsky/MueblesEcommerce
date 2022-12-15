from django.db import models
import datetime
import os
from django.contrib.auth.models import User
# Create your models here.
def get_file_path(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%d%m%Y%H:%M:%S')
    filename = "%s%s" % (nowTime, original_filename)
    return  os.path.join('uploads/', filename)

class Category(models.Model):
    slug = models.CharField(max_length=150, null=False , blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    description = models.TextField(max_length=500, null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0=disponible, 1=Oculto ")
    trending =  models.BooleanField(default=False, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.CharField(max_length=150, null=False , blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    product_image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    description = models.TextField(max_length=500, null=False, blank=False)
    small_description = models.TextField(max_length=500, null=False, blank=False)   
    quantity = models.IntegerField(null=False, blank=False) 
    original_price = models.FloatField(null=False, blank=False)
    final_price = models.FloatField(null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0=disponible, 1=Oculto ")
    trending =  models.BooleanField(default=False, null=False, blank=False , help_text="1=poner en el carrousel, 0=quitar de carrusel")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
     