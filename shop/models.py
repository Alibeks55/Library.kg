from django.db import models


class Category(models.Model):
    name_category = models.CharField(max_length=100, verbose_name='Категории:')

    def __str__(self):
        return self.name_category
    
    class Meta:
       verbose_name = 'Категорий'
       verbose_name_plural = 'Категории'



class Product(models.Model):
    name_product = models.CharField(max_length=100, verbose_name='Продукт:')
    price_product = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена продукта:')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категории:')

    def __str__(self):
        return self.name_product
    
    class Meta:
       verbose_name = 'Продукт'
       verbose_name_plural = 'продукты'


