from django.db import models

# Create your models here.
class Employee_data(models.Model):
    name = models.CharField(max_length=20)
    company = models.CharField(max_length=20)
    employee_id = models.IntegerField()
    