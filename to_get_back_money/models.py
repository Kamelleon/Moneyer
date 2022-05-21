from django.db import models

# Create your models here.
class GetBackMoney(models.Model):
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=5,decimal_places=2)
    short_description = models.CharField(max_length=100)
