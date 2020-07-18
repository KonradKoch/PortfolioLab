from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=60)


class Institution(models.Model):
    TYPES = (
        ('FUND', 'fundacja'),
        ('ORG', 'organizacja pozarządowa'),
        ('LOCAL', 'zbiórka lokalna')
    )
    name = models.CharField(max_length=60)
    description = models.TextField()
    type = models.CharField(max_length=25, choices=TYPES, default='FUND')
    categories = models.ManyToManyField(Category)


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=9)
    city = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=6)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, default=None)
