from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import random
from datetime import datetime
from . import book

def booksDetailView(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(book.Book, id=id)
        context = {
            'book_id': book_id
        } 
    return render(request, template_name='books/book_detail.html', context=context)

def booksView(request):
    if request.method == 'GET':
         books = book.Book.objects.all()
         context = {
             'book': books,
         }
    return render(request, template_name='books/book.html', context=context)






def about_me_view(request):
    if request.method == 'GET':
        me = ['Привет! Меня зовут Алибек Ниязбеков.' \
              ' Мне 18 лет, я живу в Кыргызстане и учусь в 11 классе.' \
              ' Я увлекаюсь IT и спортом, особенно программированием, тренировками в зале и боксом.' \
              ' В будущем хочу развиваться в сфере технологий и стать профессиональным разработчиком.']
        about_me = 'Обо мне: \n' + '\n'.join(me)
        return HttpResponse(about_me)
    
def time_of_day_view(request):
    if request.method == 'GET':
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

def quotes_of_great_writers_view(request):
    if request.method == 'GET':
        random_phrases = ['"Сложнее всего начать действовать, все остальное зависит только от упорства". Амелия Эрхарт, писательница и летчица',
                          '"Жизнь — это то, что с тобой происходит, пока ты строишь планы". Джон Леннон, музыкант',
                          '"Начинать всегда стоит с того, что сеет сомнения". Борис Стругацкий, писатель',
                          '"Лучшее время, чтобы посадить дерево, было 20 лет назад. Следующий подходящий момент — сегодня". Китайская пословица',
                          '"Счастье не в том, чтобы делать всегда, что хочешь, а в том, чтобы всегда хотеть того, что делаешь". Лев Толстой, писатель']
        return HttpResponse(random.choice(random_phrases))

           


