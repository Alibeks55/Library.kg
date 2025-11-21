from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout
from . import models
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class FilmListView(generic.ListView):
    template_name = 'CineBoard/films.html'
    model = models.Film
    context_object_name = 'films'

    def get(self, request, *args, **kwargs):
        films = models.Film.objects.all().order_by('-id')
        search_query = request.GET.get('s', '')
        genre = request.GET.get('genre', '')
        if search_query:
            films = films.filter(name__icontains=search_query)
        if genre:
            films = films.filter(genre=genre)
        context = {
            'films': films,
            's': search_query,
            'selected_genre': genre
        }
        return render(request, self.template_name, context)


class FilmDetailView(generic.View):
    def get(self, request, id):
        film = get_object_or_404(models.Film, id=id)
        comments = film.comments.all().order_by('-created_at')
        return render(request, 'CineBoard/film_detail.html', {'film': film, 'comments': comments})

    def post(self, request, id):
        if not request.user.is_authenticated:
            return redirect('cine_login')

        film = get_object_or_404(models.Film, id=id)
        text = request.POST.get('text', '').strip()
        if text:
            models.Comment.objects.create(film=film, user=request.user, text=text)
        return redirect('film_detail', id=film.id)


class FilmCreateView(generic.CreateView):
    model = models.Film
    template_name = 'CineBoard/film_create.html'
    fields = ['name', 'description', 'genre', 'release_date', 'rating', 'tags', 'image']
    success_url = '/'


class FilmUpdateView(generic.UpdateView):
    model = models.Film
    template_name = 'CineBoard/film_update.html'
    fields = ['name', 'description', 'genre', 'release_date', 'rating', 'tags', 'image']
    success_url = '/'

    def get_object(self):
        return models.Film.objects.get(id=self.kwargs['id'])

        
class FilmDeleteView(generic.View):
    def get(self, request, id):
        film = get_object_or_404(models.Film, id=id)
        return render(request, 'CineBoard/film_delete.html', {'film': film})

    def post(self, request, id):
        film = get_object_or_404(models.Film, id=id)
        film.delete()
        return redirect('cine_film_list') 


class SearchView(generic.View):
    def get(self, request):
        query = request.GET.get('s', '')  
        genre = request.GET.get('genre', '')  
        films = models.Film.objects.all()

        if query:
            films = films.filter(name__icontains=query)
        if genre:
            films = films.filter(genre=genre)

        context = {
            'films': films,
            's': query,
            'selected_genre': genre
        }
        return render(request, 'CineBoard/films.html', context)


class RegisterView(generic.View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'CineBoard/register.html', {"form": form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cine_login')
        return render(request, 'CineBoard/register.html', {"form": form})


class AuthLoginView(generic.View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'CineBoard/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('cine_film_list') 
        return render(request, 'CineBoard/login.html', {'form': form})
    

class AuthLogoutView(generic.View):
    def get(self, request):
        logout(request)
        return redirect('cine_film_list')
    
