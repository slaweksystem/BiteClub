from django.http import HttpRequest, HttpResponse

from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

from .models import *

# Create your views here.
@require_http_methods(["GET"])
def dinner_sessions_list(request: HttpRequest):
    if request.user.groups.filter(name='Admin').exists():
        sessions
    return render(request, 'dinner-sessions/ds-list.html')

@login_required('users/login')
@require_http_methods(["GET", "POST", "PUT", "DELETE"])
def dinner_session(request: HttpRequest, id_session):
    if request.method == "GET":
        # Admin sees all
        if request.user.groups.filter(name='Admin').exists():
            sessions

        if request.user.groups.filter(name='Manager').exists():
            pass
        session = DinnerSession.objects.get(id=id_session)
        return render(request, 'dinner-sessions/ds-list.html')
    

    
    if request.method == "POST":
        return render(request, 'dinner-sessions/ds-list.html')
    
    elif request.method == "PUT":
        return render(request, 'dinner-sessions/ds-list.html')
    
    elif request.method == "DELETE":
        return render(request, 'dinner-sessions/ds-list.html')
        