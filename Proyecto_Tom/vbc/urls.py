from django.urls import path, include
from vbc import views

urlpatterns = [
    path('product/list', views.ProductListView.as_view(), name="ProductList"),
    path('product/<pk>', views.ProductDeleteView.as_view(), name="ProductDelete"),
    path('product/<pk>/update', views.ProductUpdateView.as_view(), name="ProductUpdate"),
]