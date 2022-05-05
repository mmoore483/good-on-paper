from django.db import models
from django.contrib.auth.models import User

from django_countries.fields import CountryField

class Customer(models.Model):
    """
    A user profile model for maintaining delivery information
    and order history
    """
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    street_address1 = models.CharField(max_length=80, null=True, blank=True)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(blank_label='Country', null=True, blank=True)

    def __str__(self):
        return self.customer