from django.urls import path
from . import views

app_name = 'app_dinner_sessions'

urlpatterns = [
    path('', views.dinner_sessions_list, name="list"),
]