from django.db import models

class Caterory_Clothes(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории:')

    def __str__(self):
        return self.name
    
    class Meta:
       verbose_name = 'в Хэштеги'
       verbose_name_plural = 'Категории'
      

class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название продукта:')
    description = models.TextField(default='Описание продукта', verbose_name='Описание продукта:')
    tags = models.ManyToManyField(Caterory_Clothes, verbose_name='Выбор категории:')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}-{','.join(i.name for i in self.tags.all() )}'
    
    class Meta:
       verbose_name = 'в Хэштеги'
       verbose_name_plural = 'Продукты'
