from django.shortcuts import render, redirect ,get_object_or_404 
from . import models, forms
from  books.models import Book

def order_List_View(request):
    if request.method == 'GET':
        order = models.Placing_an_order.objects.all().order_by('-id')
    return render(request, 'BASKET/order_list.html', {'order': order}) 

def add_order(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = forms.OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            order.name_book.add(book)
            return redirect('order_list')
    else:
        form = forms.OrderForm()
    return render(request, 'BASKET/order_add.html', {'book': book, 'form': form})


def update_order(request, id):
    order_id = get_object_or_404(models.Placing_an_order, id=id)
    if request.method == 'POST':
        form = forms.OrderForm(request.POST, instance=order_id)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
         form = forms.OrderForm(instance=order_id)
    return render(request, 'BASKET/order_update.html', {'form': form, 'order_id': order_id})

def delete_order(request, id):
    order = get_object_or_404(models.Placing_an_order, id=id)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')
    return render(request, 'BASKET/order_delete.html', {'order': order})

