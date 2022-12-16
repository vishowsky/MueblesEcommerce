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

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,  on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    user = models.ForeignKey( User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=150, null=False)
    lname = models.CharField(max_length=150, null=False)
    rut = models.IntegerField(max_length=150, null=False)
    email = models.CharField(max_length=150, null=False)
    phone = models.CharField(max_length=150, null=False)
    address = models.TextField(null=False)
    city = models.CharField(max_length=150, null=False)
    region = models.CharField(max_length=150, null=False)
    total_price = models.FloatField(null=False)
    payment_mode = models.CharField(max_length=150, null=False)
    payment_id = models.CharField(max_length=250, null=True)
    orderstatuses = (
        ('pendiente','pendiente'),
        ('enviado', 'enviado'),
        ('completado','completado'),
    )
    status = models.CharField(max_length=150, choices=orderstatuses, default='pendiente')
    message = models.TextField(null=True)
    tracking_no = models.CharField(max_length=150, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return '{} - {}'.format(self.id, self.tracking_no)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(null=False)
    quantity = models.IntegerField(null=False)

    def __str__(self):
        return '{} {}'.format(self.order.id, self.order.tracking_no)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=50, null=False)
    lname = models.CharField(max_length=50, null=False)
    rut = models.IntegerField(max_length=50, null=False)
    email = models.CharField(max_length=50, null=False)
    phone = models.CharField(max_length=50, null=False)
    address = models.TextField(max_length=50, null=False)
    city = models.CharField(max_length=50, null=False)
    region = models.CharField(max_length=50, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username