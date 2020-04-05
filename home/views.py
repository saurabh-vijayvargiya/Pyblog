from django.shortcuts import render, HttpResponse

# Create your views here.

# Creating index function
def index(request):
    return HttpResponse('This is homepage')