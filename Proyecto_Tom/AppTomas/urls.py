from django.urls import path
from AppTomas import views

urlpatterns = [
    path('', views.inicio),
]