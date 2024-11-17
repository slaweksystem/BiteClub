from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from .models import Restaurant, Menu_Item
from . import forms

# Create your views here.
@require_http_methods(['GET'])
def restaurants_list(request: HttpRequest):
    if request.user.groups.filter(name='Manager').exists() or \
        request.user.groups.filter(name='Admin').exists():
        is_manager = True
    else:
        is_manager = False
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurants/restaurant_list.html',
                  {'restaurants': restaurants, 'is_manager': is_manager})

@require_http_methods(['GET'])
def restaurant_page(request: HttpRequest, id_restaurant: int):
    restaurant = Restaurant.objects.get(id=id_restaurant)
    if restaurant.owner == request.user:
        is_owner = True
    else:
        is_owner = False
    items = Menu_Item.objects.filter(restaurant=restaurant)
    return render(request, 'restaurants/restaurant_page.html',
                  {'restaurant': restaurant, 'items': items, 'is_owner': is_owner})


@require_http_methods(['GET', 'POST'])
@login_required(login_url="/users/login/")
def restaurant_new(request: HttpRequest):
    if not request.user.groups.filter(name='Manager').exists():
        return redirect('forbidden')

    if request.method == 'POST':
        form = forms.CreateRestaurant(request.POST, request.FILES)
        if form.is_valid():
            newrestaurant = form.save(commit=False)
            newrestaurant.owner = request.user
            newrestaurant.save()
            return redirect('restaurants:list')
    else:
        form = forms.CreateRestaurant()
    return render(request, 'restaurants/restaurant_new.html',{ 'form': form })

@login_required(login_url="/users/login/")
def restaurant_new_menu_item(request: HttpRequest, id_restaurant: int):
    restaurant = get_object_or_404(Restaurant, id=id_restaurant)
    if restaurant.owner != request.user:
        return redirect('forbidden')

    if request.method == 'POST':
        form = forms.CreateMenuItem(request.POST, request.FILES)
        if form.is_valid():
            newitem = form.save(commit=False)
            newitem.restaurant = restaurant
            newitem.save()
            return redirect('restaurants:list')
    else:
        form = forms.CreateMenuItem(request.POST, request.FILES)
    return render(request, 'restaurants/restaurant_new_item.html',{ 'form': form, 'restaurant': restaurant})

@login_required(login_url="/users/login/")
def restaurant_new_menu_item(request: HttpRequest, id_restaurant: int):
    restaurant = get_object_or_404(Restaurant, id=id_restaurant)
    if restaurant.owner != request.user:
        return redirect('forbidden')

    if request.method == 'POST':
        form = forms.CreateMenuItem(request.POST, request.FILES)
        if form.is_valid():
            newitem = form.save(commit=False)
            newitem.restaurant = restaurant
            newitem.save()
            return redirect('restaurants:list')
    else:
        form = forms.CreateMenuItem(request.POST, request.FILES)
    return render(request, 'restaurants/restaurant_new_item.html',{ 'form': form, 'restaurant': restaurant}) 

@login_required(login_url="/users/login/")
def restaurant_edit(request: HttpRequest, id_restaurant: int):
    restaurant = get_object_or_404(Restaurant, id=id_restaurant)
    if request.method == 'POST':
        form = forms.EditRestaurant(request.POST, request.FILES, instance=restaurant)
        if form.is_valid():
            form.save()
            messages.success(request, "Restaurant details updated successfully.")
            return redirect('restaurants:list')  # Redirect to a restaurant detail page
    else:
        form = forms.EditRestaurant(instance=restaurant)

    context = {
        'form': form,
        'restaurant': restaurant,
    }
    return render(request, 'restaurants/restaurant_edit.html', context)
