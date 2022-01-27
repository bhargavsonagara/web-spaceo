from django.db import models
from enum import Enum


dict = {
    "a" : "Automatic",
    "m" : "Manual"
}
    
    
# Create your models here.
class Product(models.Model):
    iProductId = models.AutoField(primary_key=True)
    vTitle = models.CharField(max_length=255,verbose_name='Product Title')
    vTitle1 = models.CharField(max_length=255)
    vSystem = models.CharField(max_length=255, choices=[(x, dict[x]) for x in dict])
    dPrice = models.DecimalField(decimal_places=2,max_digits=10)
    dPriceF = models.FloatField(max_length=10)
    pDate = models.DateField("Date (mm/dd/yy)", auto_now_add=False, null = True, auto_now=False, blank=True)
    pDateTime = models.DateTimeField("Date (mm/dd/yy)", auto_now_add=False, null = True, auto_now=False, blank=True)

# from bhargav.models import Product
# d = datetime.now()
# product_object = Product.objects.create(date = d)
# product_object.save()

# def __str__(self) -> str:
#     return self.vTitle