from eBook.models import Book, Writer, Clients
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
        books = Book.objects.filter(state=0)
        context['books'] = books
        return context

class BooksBiblioteca(ListView, LoginRequiredMixinStaff):
    model = Writer
    template_name = 'books/client/biblioteca.html'

    def get_context_data(self, **kwargs):
        context = super(BooksBiblioteca, self).get_context_data(**kwargs)
        context['writer'] = Writer
        return context
class BooksBibliotecaSinSession(ListView, LoginRequiredMixinStaff):
    model = Writer
    template_name = 'home/biblioteca.html'

    def get_context_data(self, **kwargs):
        context = super(BooksBibliotecaSinSession, self).get_context_data(**kwargs)
        context['writer'] = Writer
        return context
class BooksPublish(ListView, LoginRequiredMixinStaff):
    model = Writer
    template_name = 'books/client/biblioteca.html'

    def get_context_data(self, **kwargs):
        context = super(BooksPublish, self).get_context_data(**kwargs)
        context['writer'] = Writer
        return context

class EditarPerfil(ListView, LoginRequiredMixinStaff):
    model = Clients
    template_name='books/client/editarPerfil.html'

    def get_context_data(self, **kwargs):
        context = super(EditarPerfil, self).get_context_data(**kwargs)
        member = get_member(self.request.user)
        context['client'] = Clients(member)
        return context
