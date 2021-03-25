from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=120) # max length required
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10000, decimal_places=2)
    summary = models.TextField(default='this is cool')
    featured = models.BooleanField() # null=True, default=True