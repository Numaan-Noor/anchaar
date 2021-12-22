from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class product(models.Model):
    image = models.FileField()
    Name = models.CharField(max_length=500)
    price = models.IntegerField()

    def __str__(self):
        return "{}".format(self.image)


class backimage(models.Model):
    Image = models.FileField()
    name = models.CharField(max_length=50, null=True)
    adress = models.CharField(max_length=1000, null=True)
    number = models.CharField(max_length=20, null=True)

    def __str__(self):
        return "{}".format(self.Image)
