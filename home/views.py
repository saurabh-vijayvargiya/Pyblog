from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact

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
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        needs = request.POST.get('needs')
        message = request.POST.get('message')

        contact = Contact(firstname=firstname, lastname=lastname, email=email, needs=needs, message=message, date=datetime.today())
        contact.save()
        
    return render(request, 'contact.html')

# Creating index function
def services(request):
    return render(request, 'services.html')