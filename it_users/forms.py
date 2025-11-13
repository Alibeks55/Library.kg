from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField

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

class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=14, required=True, label='Телефон:')
    gender = forms.ChoiceField(choices=GENDER, required=True, label='Пол:')
    age = forms.CharField(required=True, label='Лет:')
    portfolio_link = forms.URLField(required=True, label='ссылка (на github):')
    experience_years = forms.ChoiceField(choices=YEARS, required=True,label='Опыт работы:')
    it_direction = forms.ChoiceField(choices=IT_DIRECTIONS, required=True, label='Напрвления:')
    captcha = CaptchaField(label='Ведите символ с картинки:' )

    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'password1',
            'password2',
            'email',
            'first_name',
            'last_name',
            'gender',
            'phone_number',
            'age',
            'portfolio_link',
            'experience_years',
            'it_direction'
        )

    def save(self, commit=True):
        user = super(CustomRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.phone_number = self.cleaned_data['phone_number']
        user.gender = self.cleaned_data['gender']
        user.age = self.cleaned_data['age']
        user.portfolio_link = self.cleaned_data['portfolio_link']
        user.experience_years = self.cleaned_data['experience_years']
        user.it_direction = self.cleaned_data['it_direction']
        if commit:
            user.save()
        return user