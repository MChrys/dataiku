from django.db import models


class AuthorContainer(models.Model):
    created_on = models.DateField(auto_now=True, null=True)


class Author(models.Model):
    author_container = models.OneToOneField(AuthorContainer)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{ self.first_name} { self.last_name }'

    

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True, blank=True)
    isbn = models.CharField(max_length=255, null=True, blank=True)