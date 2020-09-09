from django.urls import path
from . import views

urlpatterns = [
    path('', views.author_books_formset, name='author'),
    path('author/', views.AuthorList.as_view())
]