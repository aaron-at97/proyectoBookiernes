from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpRequest
from django.shortcuts import render

from eBook.models import Book
from django.views.generic import ListView, CreateView
from eBook.views import get_member
from eBook.views import LoginRequiredMixinStaff
from eBook.forms import BookForm


class BooksList(ListView, LoginRequiredMixinStaff):
    model = Book
    template_name = 'books/staff_book_list.html'

    def get_context_data(self, **kwargs):
        context = super(BooksList, self).get_context_data(**kwargs)
        member = get_member(self.request.user)
        if member.role == "Writer":
            books = Book.objects.filter(state=0)
            context['books'] = books
            return context


def BookCreate(request):
    context = {}
    form = BookForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "books/create_book.html", context)








