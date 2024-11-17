from django.http import HttpRequest, HttpResponseNotAllowed
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User, Group
from .forms import CustomUserCreationForm


# Create your views here.

def change_password_view(request: HttpRequest):
    if request.method == "POST":
        form = PasswordChangeForm(data = request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("users:list")
    else:
        form = PasswordChangeForm()
    return render(request, 'users/change_password.html', {"form": form}) 

def register_view(request: HttpRequest):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            customer_group, created = Group.objects.get_or_create(name='Customer')
            user.groups.add(customer_group)

            login(request, user)
            return redirect("dinner-sessions:list")
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {"form": form})

def login_view(request: HttpRequest):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect("dinner-sessions:list")
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {"form": form})

def logout_view(request: HttpRequest):
    if request.method == "POST":
        logout(request)
        return render(request, 'users/logout.html')
    return HttpResponseNotAllowed(["POST"])

def user_profile_view(request: HttpRequest):
    return render(request, 'users/user_profile.html')