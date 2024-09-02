from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from AppTomas.models import Product

class ProductListView(ListView):
    model = Product
    context_object_name = 'Products'
    template_name = 'vbc/product_list.html'
    
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'vbc/product_delete.html'
    success_url = reverse_lazy('ProductList')
    
class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'price']
    template_name = 'vbc/product_update.html'
    success_url = reverse_lazy('ProductList')