from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home_page_view(request):
    return HttpResponse("<h1>Hello, World! Welcome to Django.</h1>")