from django.urls import path
from . import views

app_name = 'app_restaurants'

urlpatterns = [
    path('', views.restaurants_list, name="list"),
    path('new-restaurant/', views.restaurant_new, name="new-restaurant"),
    path('<int:id_restaurant>', views.restaurant_page, name="restuarant"),
    path('<int:id_restaurant>/new-menu-item/', views.restaurant_new_menu_item, name="new-menu-item"),
    path('<int:id_restaurant>/edit-restaurant/', views.restaurant_edit, name="edit-restaurant"),
]