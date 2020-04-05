from django.shortcuts import render, HttpResponse

# Create your views here.

# Creating index function
def index(request):
    return HttpResponse('This is homepage')

# Creating index function
def about(request):
    return HttpResponse('This is about page')

# Creating index function
def contact(request):
    return HttpResponse('This is contact page')

# Creating index function
def services(request):
    return HttpResponse('This is services page')    