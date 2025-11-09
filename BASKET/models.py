from django.db import models
from books.models import Book

class Placing_an_order(models.Model):
    city_KG = (
        ('Бишкек','Бишкек'),
        ('Ош','Ош'),
        ('Каракол','Каракол'),
        ('Джалал-Абад','Джалал-Абад'),
        ('Токмок','Токмок'),
        ('Нарын','Нарын'),
        ('Талас','Талас')
    )

    payment_method = (
        ('картой','картой'),
        ('наличкой','наличкой')
    )

    user_full_name = models.CharField(max_length=100, verbose_name='Ваше ФИО:')
    user_phone = models.IntegerField(max_length=10, verbose_name='Ваш номер телефона:')
    user_city = models.CharField(max_length=100, choices=city_KG, verbose_name='Ваш город:')
    user_address = models.CharField(max_length=100, verbose_name='Ваш адрес:')
    user_payment_method = models.CharField(choices=payment_method, verbose_name='Способ оплаты:')

    name_book = models.ManyToManyField(Book, related_name='orders', verbose_name='Книги:')

    def __str__(self):
      return self.user_full_name



