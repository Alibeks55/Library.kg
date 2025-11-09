from django import forms
from . import models

class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Placing_an_order
        fields = '__all__' 