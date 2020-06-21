from django.db import models

# Create your models here.

class Goods(models.Model):
  product = models.CharField(max_length=100)
  price = models.IntegerField(help_text='Price')

  def __str__(self):
    return self.product
