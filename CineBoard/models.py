from django.db import models
from django.contrib.auth.models import User

class Ratihg(models.Model):
    value = models.IntegerField()

    def __str__(self):
        return str(self.value)
    
    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'
    

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Film(models.Model):
    GENRE = (
   ('фантастика', 'Фантастика'),
   ('Ужасы', 'Ужасы'),
   ('Мелодрамма', 'Мелодрамма'),
   ('Боевик', 'Боевик')
)

    name = models.CharField(max_length=100, verbose_name='Введите название фильма:')
    description = models.TextField(verbose_name='Укажите описание фильма:')
    genre = models. CharField(max_length=100, choices=GENRE, verbose_name='Укажите жанр:')
    release_date = models.DateField(verbose_name='Дата выхода фильма:')
    rating = models.ForeignKey(Ratihg, on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    image = models.ImageField(upload_to='films/', verbose_name='загрузите фото')

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.text[:20]}'
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
    
    




