from eBook.auth_views import LoginView
from django.urls import path
from django.conf.urls import url
from eBook.books_view import BooksList, home_view

urlpatterns = [
    url(r'^$', LoginView.as_view(), name="login"),
    path('list_books/', BooksList.as_view(), name="list_book"),
    path('book_create/', home_view, name='book_create'),
]