from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def dinner_sessions_list(request: HttpRequest):
        return render(request, 'dinner-sessions/ds-list.html')