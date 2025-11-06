from django.db import models
from django.contrib.auth.models import User

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

    def overall_rating(self):
     
     current_rating = 10.0

     for grade in self.reviews.all():
        if grade.mark == '1' and current_rating > 0:
            current_rating -= 0.5
        elif grade.mark == '2' and current_rating > 0:
            current_rating -= 0.2
        elif grade.mark == '3':
            pass  
        elif grade.mark == '4' and current_rating < 10:
            current_rating += 0.2
        elif grade.mark == '5' and current_rating < 10:
            current_rating += 0.5

     current_rating = max(0, min(10, current_rating))
     return round(current_rating, 1)

#python manage.py makemigrations
#python manage.py migrate


class Reviews(models.Model):
  MARK =(
      ('1','1'),
      ('2','2'),
      ('3','3'),
      ('4','4'),
      ('5','5')
   )
  
  choice_book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews', verbose_name='Книги:')
  name_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
  mark = models.CharField(max_length=100, choices=MARK, default='5', verbose_name='Оценка:')
  comments = models.TextField(verbose_name='комментарий:')

  def __str__(self):
      return f'{self.choice_book}-{self.mark}'
   
  class Meta:
    verbose_name = 'комментарий'
    verbose_name_plural = 'Комментарии' 

       
