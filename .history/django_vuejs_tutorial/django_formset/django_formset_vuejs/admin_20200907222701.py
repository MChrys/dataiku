from django.contrib import admin
from .models import AuthorContainer, Author, Book
# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(AuthorContainer)