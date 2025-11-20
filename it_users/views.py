from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from . import models, forms
from .forms import CustomRegisterForm, CustomAuthenticationForm

from django.views import generic 


class RegisterView(generic.View):
    def get(self, request):
        form = forms.CustomRegisterForm()
        return render(request, 'it_users/register.html', {"form": form})
    def post(self, request):
        form = forms.CustomRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
        return render(request, 'it_users/register.html', {"form": form})


class AuthLoginView(generic.View):
    def get(self, request):
        form = forms.CustomAuthenticationForm()
        return render(request, 'it_users/login.html', {'form': form})

    def post(self, request):
         form = forms.CustomAuthenticationForm(data=request.POST)
         if form.is_valid:
             user = form.get_user()
             login(request, user)
             return redirect('it_users:user_list')
         return render(request, 'it_users/login.html', {'form': form})


class AuthLogoutView(generic.View):
    def get(self, request):
        logout()
        return redirect('it_users:login')


class ItUserListView(generic.ListView):
    model = models.CustomUser
    template_name = 'it_users/id_user_list.html'
    context_object_name = 'users'
    ordering = ['-id']





# def registerView(request):
#     if request.method == 'POST':
#         form = forms.CustomRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/login/')
#     else:
#         form = forms.CustomRegisterForm()
#     return render(request, 'it_users/register.html', {'form': form})
    

# def authloginView(request):
#     if request.method == 'POST':
#         form = forms.CustomAuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('it_users:user_list')
#     else:
#         form = forms.CustomAuthenticationForm()
#     return render(request, 'it_users/login.html', {'form': form})


# def authLogoutView(request):
#     logout(request)
#     return redirect('it_users:login')


# def it_user_list_view(request):
#     if request.method == 'GET':
#         users = models.CustomUser.objects.all().order_by('-id')
#     return render(request, 'it_users/id_user_list.html', {'users': users})