from django.urls import path
from AppTomas import views

urlpatterns = [
    path('', views.index, name="Home"),
    path('about/', views.contact, name="About"),
]