from django.urls import path
from . import views

app_name = 'app_users'

urlpatterns = [
    path('login/', views.login_view, name ="login"),
    path('logout/', views.logout_view, name="logout"),
    path('register/', views.register_view, name="register"),
    path('user_profile/', views.user_profile_view, name="user_profile"),
    path('change_password/', views.change_password_view, name="change_password"),
]