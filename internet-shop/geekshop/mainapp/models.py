from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name="имя", max_length=100)
    description = models.TextField(verbose_name="описание", blank=True)
    is_active = models.BooleanField(verbose_name="активна", default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="имя", max_length=100)
    price = models.DecimalField(
        verbose_name="цена", max_digits=7, decimal_places=2, default=0
    )
    color = models.TextField(verbose_name="цвет", blank=True)
    description = models.TextField(verbose_name="описание", blank=True)
    image = models.ImageField(verbose_name="картинка", blank=True, upload_to="products")
    quantity = models.PositiveIntegerField(verbose_name="количество", default=0)
    is_active = models.BooleanField(verbose_name="активен", default=True)

    def __str__(self):
        return self.name
