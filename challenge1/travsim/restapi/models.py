from django.db import models

# Create your models here.

class Goods(models.Model):
  product = models.CharField(max_length=100)
  price = models.DecimalField(max_digits=20, decimal_places=2, help_text='Price')

  def __str__(self):
    return self.product
