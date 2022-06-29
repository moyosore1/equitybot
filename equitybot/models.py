from django.db import models

# Create your models here.


class Equity(models.Model):
    market_watch = models.TimeField()
    equity = models.DecimalField(max_digits=10, decimal_places=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['-id']
