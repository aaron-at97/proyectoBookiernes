from eBook.models import Book
from django.views.generic import ListView
from eBook.views import get_member
from eBook.views import LoginRequiredMixinStaff

class BooksImageList(ListView, LoginRequiredMixinStaff):
    model = Book
    template_name = 'books/diseñador/book_list_diseny.html'

    def get_context_data(self, **kwargs):
        context = super(BooksImageList, self).get_context_data(**kwargs)
        books = Book.objects.filter(state=0)
        context['books'] = books
        return context

class BooksPublishList(ListView, LoginRequiredMixinStaff):
    model = Book
    template_name = 'books/maquetador/book_list_publish.html'

    def get_context_data(self, **kwargs):
        context = super(BooksPublishList, self).get_context_data(**kwargs)
        member = get_member(self.request.user)
        books = Book.objects.filter(state=0)
        context['books'] = books
        return context
