from django.db import models

from user.models import MarketUser


# Create your models here.


class Executor(models.Model):
    user: MarketUser = models.ForeignKey(MarketUser, on_delete=models.CASCADE)




class Customer(models.Model):
    user = models.ForeignKey(MarketUser, on_delete=models.CASCADE)
