from django.db import models

# Create your models here.
class Contact(models.Model) :
    firstname = models.CharField(max_length=122)
    lastname = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    needs = models.CharField(max_length=50)
    message = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.firstname + ' ' + self.lastname

# Create Author model
class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()

# Create category model
class Category(models.Model):
    category = models.CharField(max_length=100)
    description = models.TextField()

# Create Article model
class Article(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/')
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
