from django.contrib import admin
from home.models import Contact
from home.models import Article
from home.models import Author
from home.models import Category

# Register your models here.
admin.site.register(Contact)
admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Category)