from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from . import models, forms
from .forms import CustomRegisterForm


def registerView(request):
    if request.method == 'POST':
        form = forms.CustomRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = forms.CustomRegisterForm()
    return render(request, 'it_users/register.html', {'form': form})
    

def authloginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('it_users:user_list')
    else:
        form = AuthenticationForm()
    return render(request, 'it_users/login.html', {'form': form})


def authLogoutView(request):
    logout(request)
    return redirect('it_users:login')


def it_user_list_view(request):
    if request.method == 'GET':
        users = models.CustomUser.objects.all().order_by('-id')
    return render(request, 'it_users/id_user_list.html', {'users': users})