from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from datetime import datetime


class Contact(models.Model):
    listing =models.CharField(max_length = 200)
    listing_id = models.IntegerField()       
    name = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)
    phone = models.CharField(max_length = 200)
    message = models.TextField(blank = True)
    contact_date = models.DateTimeField(default = datetime.now, blank = True)
    user_id = models.IntegerField(blank = True)

    def __str__(self):
        return self.name

class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField()
    description = models.TextField(blank=True)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    is_mvp = models.BooleanField(default=True)
    hire_date = models.DateTimeField(default = datetime.now, blank = True)

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("category", kwargs={
            'slug': self.slug
        })

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url



class Property(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete = models.DO_NOTHING)
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    slug = models.SlugField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    image = models.ImageField()
    photo_1 = models.ImageField(blank=True)
    photo_2 = models.ImageField(blank=True)
    photo_3 = models.ImageField(blank=True)
    photo_4 = models.ImageField(blank=True)
    photo_5 = models.ImageField(blank=True)
    photo_6 = models.ImageField(blank=True)
    photo_7 = models.ImageField(blank=True)
    list_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
    #{{ item.get_absolute_url }}
        return reverse("listing", kwargs={'slug': self.slug})


class PropertySearch(models.Model):
    state = models.CharField(max_length=13)
    AreaOfInterest = models.CharField(max_length=19)
    features = models.CharField(max_length=123)
    description = models.TextField()