from django.db import models

class Book(models.Model):
    GENRE = (
   ('Фантастика', 'Фантастика'),
   ('Ужасы', 'Ужасы'),
   ('Мелодрамма', 'Мелодрамма'),
   ('Боевик', 'Боевик'),
   ('Классика','Классика')
)
   
    title = models.CharField(max_length=100, verbose_name='введите название книги')
    image = models.ImageField(upload_to='book/', verbose_name='загрузите фото')
    description = models.TextField(verbose_name='Укажите описание книги')
    director = models.CharField(max_length=100, verbose_name='укажите писателя',
                                default='Николай Гоголь')
    genre = models.CharField(max_length=100, choices=GENRE, verbose_name='Укажите жанр')
    country = models.CharField(max_length=100, default='ЕВРОПА', verbose_name='укажите страну')
    duration = models.PositiveIntegerField(verbose_name='укажите сколько страниц',
                                          default=None)
    trailer = models.URLField(verbose_name='вставьте ссылку на книгу')
    created_at = models.DateField(verbose_name='Дата добавления', null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена кники', default=0.0)

    def __str__(self):
      return self.title
    
    class Meta:
       verbose_name = 'Книга'
       verbose_name_plural = 'Книги'

#python manage.py makemigrations
#python manage.py migrate
       
