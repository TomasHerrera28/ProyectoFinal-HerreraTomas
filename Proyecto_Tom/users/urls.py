from django.urls import path
from users import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', views.login_request, name="Login"),
    path('register/', views.register, name="Register"),
    path('logout/',LogoutView.as_view(template_name='AppTomas/index.html'), name="Logout"),
    path('edit_user/', views.edit_user, name="EditUser"),
    path('change_password/', views.ChangePasswordView.as_view(), name="ChangePassword"),
]