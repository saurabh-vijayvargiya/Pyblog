from django.shortcuts import render, HttpResponse

# Create your views here.

# Creating index function
def index(request):
    # return HttpResponse('This is homepage')
    context = {
        'variable': 'This is value',
        'book': 'The Intelligent Investor'
    }
    return render(request, 'index.html', context)

# Creating index function
def about(request):
    return render(request, 'about.html')

# Creating index function
def contact(request):
    return render(request, 'contact.html')

# Creating index function
def services(request):
    return render(request, 'services.html')