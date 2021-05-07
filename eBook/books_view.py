from django.http import HttpRequest
from django.shortcuts import render

from eBook.models import Book
from django.views.generic import ListView
from eBook.views import get_member
from eBook.views import LoginRequiredMixinStaff
from eBook.forms import BookForm


class BooksList(ListView, LoginRequiredMixinStaff):
    model = Book
    template_name = 'books/escritor/staff_book_list.html'

    def get_context_data(self, **kwargs):
        context = super(BooksList, self).get_context_data(**kwargs)
        member = get_member(self.request.user)
        if member.role == "Writer":
            books = Book.objects.filter(state=0)
            context['books'] = books
            return context


class BookCreate(HttpRequest):

    def index(request):
        booklist = BookForm()
        return render(request, "books/escritor/create_book.html", {"form": booklist})

    def procesar_formulario(request):
        booklist = BookForm(request.POST)
        if booklist.is_valid():
            booklist.save()
            booklist = BookForm()
        return render(request, "books/escritor/create_book.html", {"form": booklist, "mensaje": 'OK'})
