from eBook.models import Book, Writer
from django.views.generic import ListView, TemplateView
from eBook.views import LoginRequiredMixinStaff


class BooksHome(ListView, LoginRequiredMixinStaff):
    model = Writer
    template_name = 'home/home_base.html'

    def get_context_data(self, **kwargs):
        context = super(BooksHome, self).get_context_data(**kwargs)
        context['writer'] = Writer
        return context

class BooksHome2(ListView, LoginRequiredMixinStaff):
    model = Writer
    template_name = 'books/client/general.html'

    def get_context_data(self, **kwargs):
        context = super(BooksHome2, self).get_context_data(**kwargs)
        context['writer'] = Writer
        return context

class LeerLibroSinSession(TemplateView):
    template_name = 'home/libro_SinSession.html'

    def get_context_data(self, **kwargs):
        context = super(LeerLibroSinSession, self).get_context_data(**kwargs)
        context['libro'] = self.kwargs['libropk']
        context['autor'] = self.kwargs['autor']

        return context
