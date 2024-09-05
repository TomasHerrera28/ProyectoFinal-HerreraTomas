from django.urls import path
from products import views

urlpatterns = [
    #path('product/<pk>', views.ProductDeleteView.as_view(), name="ProductDelete"),
    path('product-list/', views.ProductListView.as_view(), name="ProductList"),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name="ProductDetail"),
    path('product-update/<int:pk>', views.ProductUpdateView.as_view(), name="ProductUpdate"),
]