import datetime

from django.db import models
from django.utils import timezone
# Create your models here.
class Stock(models.Model):
    postID = models.CharField(max_length=32)
    postURL = models.CharField(max_length=500)
    stock = models.CharField(max_length=32)
    ups = models.IntegerField(blank=True)
    downs = models.IntegerField(blank=True)
    numComments = models.IntegerField(blank=True)

    def __str__(self):
        return (self.postID, self.postURL, self.stock, self.ups, self.downs, self.numComments)
