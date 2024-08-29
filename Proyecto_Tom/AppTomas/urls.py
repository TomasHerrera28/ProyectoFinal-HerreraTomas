from django.urls import path
from AppTomas import views

urlpatterns = [
    path('', views.index, name="Home"),
    path('products/', views.products, name="Products"),
    path('contact/', views.contact, name="Contact"),
    path('contact-form/', views.contact_form, name="Contact-Form"),
]