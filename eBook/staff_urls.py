from django.views.generic import TemplateView
from eBook.auth_views import LoginView
from django.urls import path
from django.conf.urls import url
from eBook.books_view import BooksList, BookCreate
from eBook.views import rolsStaff

urlpatterns = [
    url(r'^$', LoginView.as_view(), name="login"),
    path('list_books/', BooksList.as_view(), name="list_book"),
    path('book_create/', BookCreate, name='book_create'),
    path('book_publish/', TemplateView.as_view(template_name='books/editor/libros_publicados.html'), name="book_publish"),
    path('book_acept/', TemplateView.as_view(template_name='books/editor/libros_aceptados.html'), name="book_acept"),
    path('book_rejected/', TemplateView.as_view(template_name='books/editor/libros_rechazados.html'), name='book_rejected'),
    path('index/', rolsStaff.as_view(), name='rols'),
]
"""path('index/', rolsStaff.as_view(), name='rols'),"""