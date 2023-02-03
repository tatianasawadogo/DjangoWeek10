from django.db import models
from datetime import datetime

class Realtor(models.Model):
    name=models.CharField(max_length=200)
    photo=models.ImageField(upload_to='photo/%y/%m/%d')
    description=models.TextField(blank=True)
    phone=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    is_MVP=models.BooleanField(blank=True)
    hire_date=models.DateField(default=datetime.now, blank=True)


def __str__(self):
        return self.name