from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True, upload_to="ProductImages/")
    code = models.CharField(max_length=10)
    category = models.CharField(max_length= 100, null = True)
    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, parent_link=True)
    image = models.ImageField(null=True, upload_to="ExtraProductImage/")
    def __str__(self):
        return str(self.product)


class ProductInfo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, parent_link=True)
