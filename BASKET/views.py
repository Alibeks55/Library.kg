from django.shortcuts import render, redirect ,get_object_or_404 
from . import models, forms
from  books.models import Book

from django.views import generic


class OrderListView(generic.ListView):
    model = models.Placing_an_order
    template_name = 'BASKET/order_list.html'
    context_object_name = 'order'
    ordering = ['-id']


class UpdateOrderView(generic.UpdateView):
    model = models.Placing_an_order
    form_class = forms.OrderForm 
    template_name = 'BASKET/order_update.html'
    success_url = '/order_list/'

    def get_object(self, **kwargs):
        order_id = self.kwargs.get('id')
        return get_object_or_404(models.Placing_an_order, id=order_id)
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateOrderView, self).form_valid(form=form)
    

class AddOrderView(generic.CreateView):
    model = models.Placing_an_order
    form_class = forms.OrderForm
    template_name = 'BASKET/order_add.html'
    success_url = '/order_list/'
    
    def form_valid(self, form):
        book = get_object_or_404(Book, id=self.kwargs['book_id'])
        response = super().form_valid(form)
        self.object.name_book.add(book)
        return response



class DeleteOrderView(generic.DeleteView):
    model = models.Placing_an_order
    template_name = 'BASKET/order_delete.html'
    success_url = '/order_list/'
    context_object_name = 'order'

    def get_object(self, **kwargs):
        id = self.kwargs.get('id')
        return get_object_or_404(models.Placing_an_order, id=id)
    

    



# def order_List_View(request):
#     if request.method == 'GET':
#         order = models.Placing_an_order.objects.all().order_by('-id')
#     return render(request, 'BASKET/order_list.html', {'order': order}) 


# def add_order(request, book_id):
#     book = get_object_or_404(Book, id=book_id)
#     if request.method == 'POST':
#         form = forms.OrderForm(request.POST)
#         if form.is_valid():
#             order = form.save()
#             order.name_book.add(book)
#             return redirect('order_list')
#     else:
#         form = forms.OrderForm()
#     return render(request, 'BASKET/order_add.html', {'book': book, 'form': form})


# def update_order(request, id):
#     order_id = get_object_or_404(models.Placing_an_order, id=id)
#     if request.method == 'POST':
#         form = forms.OrderForm(request.POST, instance=order_id)
#         if form.is_valid():
#             form.save()
#             return redirect('order_list')
#     else:
#          form = forms.OrderForm(instance=order_id)
#     return render(request, 'BASKET/order_update.html', {'form': form, 'order_id': order_id})


# def delete_order(request, id):
#     order = get_object_or_404(models.Placing_an_order, id=id)
#     if request.method == 'POST':
#         order.delete()
#         return redirect('order_list')
#     return render(request, 'BASKET/order_delete.html', {'order': order})

