from django.db import models

# Create your models here.
class collection(models.Model):
    nameinfo = models.CharField(max_length=20)
    sex = models.CharField(max_length=20)
    num = models.CharField(max_length=20)
    tel = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    wechat = models.CharField(max_length=30)
    addr = models.CharField(max_length=20)
    position = models.CharField(max_length=20)
    sport = models.CharField(max_length=20)
    food = models.CharField(max_length=20)