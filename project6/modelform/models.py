from django.db import models

# Create your models here.
class User(models.Model):
    """
        A manually created user Model
    """
    name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)