from django.urls import path
from users import views

urlpatterns = [
    path('login/', views.login_request, name="Login"),
    path('register/', views.register, name="Register"),
    path('logout/', views.logout_request, name="Logout"),
    path('edit_user/', views.edit_user, name="EditUser"),
    path('change_password/', views.ChangePasswordView.as_view(), name="ChangePassword"),
]