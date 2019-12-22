from django.db import models
from django.db.models.signals import post_save

# Create your models here.
class hacked_account(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=50)
    uid=models.IntegerField(max_length=100)

    def __str__(self):
        return  self.username





