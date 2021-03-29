from django.db import models

# Create your models here.

class PosModel(models.Model):
    product_name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    qty = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.product_name)
