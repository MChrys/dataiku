from django.db import transaction
from django.shortcuts import render, get_object_or_404, redirect
from .models import Author, AuthorContainer, Book
from django.views.generic import ListView
from . import forms


def author_books_formset(request):
    user = request.user
    if user.is_anonymous:
        author, _ = AuthorContainer.objects.get_or_create(id=request.session.get('author_id', None))
        request.session['author_id'] = author.id
        request.session.save()
    author = get_object_or_404(AuthorContainer, id=request.session['author_id'])
    print('SESSION')
    print(vars(request.session))

    if request.method == 'POST':
        formset = forms.AuthorsFormset(request.POST or None, request.FILES, instance=author)
        with transaction.atomic():
            if formset.is_valid():
                obj = formset.save(commit=False)
                for deleted in formset.deleted_objects:
                    deleted.delete()
                for form in obj:
                    form.author_container = author
                    form.save()
                obj = formset.save()
                return redirect('author')
    else:
        formset = forms.AuthorsFormset(instance=author)

    return render(request, 'django_formset_vuejs/author.html', {
        'parent': author,
        'authors_formset': formset})

class AuthorList(ListView):
    model = Author
    context_object_name = 'author_list'
    template_name='/django_formset_vuejs/author.html'


