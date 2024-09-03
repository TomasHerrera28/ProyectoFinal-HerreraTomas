from django.urls import path
from users import views
#from django.contrib.auth.views import logout_then_login
#from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.login_request, name="Login"),
    path('register/', views.register, name="Register"),
    path('logout/', views.logout_request, name="Logout"),
    #path('logout/',logout_then_login, name="Logout"),
    #path('logout/', auth_views.LogoutView.as_view(), name='Logout'),
    path('edit_user/', views.edit_user, name="EditUser"),
    path('change_password/', views.ChangePasswordView.as_view(), name="ChangePassword"),
]