from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.
from django.urls import reverse


class ReturnMoney(models.Model):
    title = models.CharField(max_length=25)
    amount = models.DecimalField(max_digits=5,decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    short_description = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse("to-return-details",kwargs={"id":self.id})