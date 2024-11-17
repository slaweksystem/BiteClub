from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

def rootpage(request: HttpResponse):
    return redirect("home")

@login_required(login_url="/users/login/")
def homepage(request: HttpResponse):
    return render(request, 'home.html', {'data': '' })

def forbidden(request: HttpResponse):
    return render(request, 'forbidden.html', {'data': '' })