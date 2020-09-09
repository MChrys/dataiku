from django.urls import path
from . import views

urlpatterns = [
    path('author/<int:author_id>', views.author_books_formset, name='author_detail'),
    path('author/', views.AuthorList.as_view())
]