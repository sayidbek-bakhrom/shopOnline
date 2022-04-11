from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.IntegerField()
    description = models.CharField(max_length=1024)
    image_url = models.CharField(max_length=512)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home', args=str(self.id))
