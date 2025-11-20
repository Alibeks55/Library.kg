from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import random
from datetime import datetime
from . import book

from django.views import generic


class BooksListView(generic.ListView):
    template_name = 'books/book.html'
    model = book.Book
    context_object_name = 'book'
    ordering = ['-id']


class BooksDetailView(generic.DetailView):
    template_name = 'books/book_detail.html'
    model = book.Book
    pk_url_kwarg = 'id'
    context_object_name = 'book_id'
    context_overall_rating = 'overall_rating'


class SearchView(generic.ListView):
    def get(self, request):
        query = request.GET.get('s', '')
        if query:
            books = book.Book.objects.filter(title__icontains=query)
        else:
            books = book.Book.objects.none
        context = {
            'book': books,
            's': query
        }
        return render(request, template_name='books/book.html', context=context)





class AboutMeView(generic.View):
    def get(self, request):
        me = ['Привет! Меня зовут Алибек Ниязбеков.' \
              ' Мне 18 лет, я живу в Кыргызстане и учусь в 11 классе.' \
              ' Я увлекаюсь IT и спортом, особенно программированием, тренировками в зале и боксом.' \
              ' В будущем хочу развиваться в сфере технологий и стать профессиональным разработчиком.']
        about_me = 'Обо мне: \n' + '\n'.join(me)
        return HttpResponse(about_me)
    

class TimeOfDayView(generic.View):
    def get(self, request):
        now = datetime.now()
        now_hour = now.hour
        if now_hour <= 12:
            time_hour = 'Сейчас утро'
        elif 12 <= now_hour <= 14:
             time_hour = 'Сейчас день'
        elif 14 <= now_hour <= 20:
            time_hour = 'Сейчас вечер'
        else:
            time_hour = 'Сейчас ночь'
        return HttpResponse(f'Текущая время: {time_hour}')
    

class QuotesOfGreatWritersView(generic.View):
    def get(self, request):
        random_phrases = ['"Сложнее всего начать действовать, все остальное зависит только от упорства". Амелия Эрхарт, писательница и летчица',
                          '"Жизнь — это то, что с тобой происходит, пока ты строишь планы". Джон Леннон, музыкант',
                          '"Начинать всегда стоит с того, что сеет сомнения". Борис Стругацкий, писатель',
                          '"Лучшее время, чтобы посадить дерево, было 20 лет назад. Следующий подходящий момент — сегодня". Китайская пословица',
                          '"Счастье не в том, чтобы делать всегда, что хочешь, а в том, чтобы всегда хотеть того, что делаешь". Лев Толстой, писатель']
        return HttpResponse(random.choice(random_phrases))


    

        
    


# def searchView(request):
#     query = request.GET.get('s','')
#     books = book.Book.objects.filter(title__icontains=query) if query else book.Book.none
#     context = {
#         'book': books,
#         's': query
#     }
#     return render(request, template_name='books/book.html', context=context)


# def booksDetailView(request, id):
#     if request.method == 'GET':
#         book_id = get_object_or_404(book.Book, id=id)
#         overall_rating = book_id.overall_rating()
#         context = {
#             'book_id': book_id,
#             'overall_rating': overall_rating
#         } 
#     return render(request, template_name='books/book_detail.html', context=context)


# def booksView(request):
#     if request.method == 'GET':
#          books = book.Book.objects.all()
#          context = {
#              'book': books,
#          }
#     return render(request, template_name='books/book.html', context=context)





# def about_me_view(request):
#     if request.method == 'GET':
#         me = ['Привет! Меня зовут Алибек Ниязбеков.' \
#               ' Мне 18 лет, я живу в Кыргызстане и учусь в 11 классе.' \
#               ' Я увлекаюсь IT и спортом, особенно программированием, тренировками в зале и боксом.' \
#               ' В будущем хочу развиваться в сфере технологий и стать профессиональным разработчиком.']
#         about_me = 'Обо мне: \n' + '\n'.join(me)
#         return HttpResponse(about_me)


# def time_of_day_view(request):
#     if request.method == 'GET':
#         now = datetime.now()
#         now_hour = now.hour
#         if now_hour <= 12:
#             time_hour = 'Сейчас утро'
#         elif 12 <= now_hour <= 14:
#              time_hour = 'Сейчас день'
#         elif 14 <= now_hour <= 20:
#             time_hour = 'Сейчас вечер'
#         else:
#             time_hour = 'Сейчас ночь'
#     return HttpResponse(f'Текущая время: {time_hour}') 


# def quotes_of_great_writers_view(request):
#     if request.method == 'GET':
#         random_phrases = ['"Сложнее всего начать действовать, все остальное зависит только от упорства". Амелия Эрхарт, писательница и летчица',
#                           '"Жизнь — это то, что с тобой происходит, пока ты строишь планы". Джон Леннон, музыкант',
#                           '"Начинать всегда стоит с того, что сеет сомнения". Борис Стругацкий, писатель',
#                           '"Лучшее время, чтобы посадить дерево, было 20 лет назад. Следующий подходящий момент — сегодня". Китайская пословица',
#                           '"Счастье не в том, чтобы делать всегда, что хочешь, а в том, чтобы всегда хотеть того, что делаешь". Лев Толстой, писатель']
#         return HttpResponse(random.choice(random_phrases))

           


