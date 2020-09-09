from django.urls import path
from . import views

urlpatterns = [
    path('author/<int:pk>', views.author_books_formset, name='author_detail'),
    path('author/', views.AuthorList.as_view())
]