from django.db import models

# Create your models here.


class Executor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)