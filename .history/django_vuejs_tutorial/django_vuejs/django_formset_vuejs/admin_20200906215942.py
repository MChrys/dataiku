from django.contrib import admin

# Register your models here.
from .models import Author, Book,AuthorContainer, QQM

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(AuthorContainer)
admin.site.register(QCM)