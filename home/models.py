from django.db import models

# Create your models here.
class Contact(models.Model) :
    firstname = models.CharField(max_length=122)
    lastname = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    needs = models.CharField(max_length=50)
    message = models.TextField()
    date = models.DateField()