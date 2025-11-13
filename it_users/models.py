from django.db import models
from django.contrib.auth.models import User


class CustomUser(User):
    YEARS = (
        ('1-3', '1-3'),
        ('4-6', '4-6'),
        ('7-10', '7-10'),
        ('+10', '+10')
    )

    GENDER = (
        ('мужкой', 'мужкой'),
        ('женский', 'женский')
    )

    IT_DIRECTIONS = (
    ('Backend', 'Backend'),
    ('Frontend', 'Frontend'),
    ('Fullstack', 'Fullstack'),
    ('Mobile', 'Mobile'),
    ('Devops', 'Devops'),
    ('Datascience', 'Datascience'),
    ('QA', 'QA'),
    ('UI/UX', 'UI/UX'),
    ('Cybersecurity', 'Cybersecurity'),
    ('Game Development', 'Game Development'),
    )
    
    phone_number = models.CharField(max_length=13, default="+996")
    portfolio_link = models.URLField()
    experience_years = models.CharField(max_length=100, choices=YEARS)
    gender_user = models.CharField(max_length=100, choices=GENDER)
    age = models.IntegerField(max_length=100, verbose_name='лет')
    it_direction = models.CharField(choices=IT_DIRECTIONS, max_length=20)




