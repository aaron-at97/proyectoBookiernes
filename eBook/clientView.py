from eBook.models import Book, Clients
from django.views.generic import ListView
from eBook.views import LoginRequiredMixinStaff

class EditarPerfil(ListView, LoginRequiredMixinStaff):
    model = Clients
    template_name='books/client/editarPerfil.html'

    def get_context_data(self, **kwargs):
        context = super(EditarPerfil, self).get_context_data(**kwargs)
        books = Book.objects.filter()
        context['client'] = Clients
        return context

