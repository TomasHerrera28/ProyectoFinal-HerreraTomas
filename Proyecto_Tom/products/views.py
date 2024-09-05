from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic import ListView
from AppTomas.models import Product
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from AppTomas.models import Product
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import UserPassesTestMixin

# VISTAS BASADAS EN CLASES - Productos

class SuperuserRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser, self.request.user.is_staff


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'products/product_list.html'
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
       
class ProductUpdateView(SuperuserRequiredMixin, UpdateView):
    model = Product
    success_url = reverse_lazy('ProductList')
    fields = ['name', 'price']
    template_name = 'products/product_update.html'
    
