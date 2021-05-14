from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from eBook.models import Editor, EditorChief, Writer, ChiefDesigner, Designer, CTO, Developer, Notification, Book


class LoginRequiredMixinStaff(object):
    @method_decorator(login_required(login_url='/staff/login'))
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


def get_member(user):
    if Writer.objects.filter(user=user).exists():
        return Writer.objects.get(user=user)
    if Editor.objects.filter(user=user).exists():
        return Editor.objects.get(user=user)
    elif EditorChief.objects.filter(user=user).exists():
        return EditorChief.objects.get(user=user)
    elif ChiefDesigner.objects.filter(user=user).exists():
        return ChiefDesigner.objects.get(user=user)
    elif Designer.objects.filter(user=user).exists():
        return Designer.objects.get(user=user)
    elif CTO.objects.filter(user=user).exists():
        return CTO.objects.get(user=user)
    elif Developer.objects.filter(user=user).exists():
        return Developer.objects.get(user=user)

    return None


class rolsStaff(TemplateView):
    second_model = Notification
    template_name = 'navbars/control_rol.html'

    def get_context_data(self, **kwargs):
        context = super(rolsStaff, self).get_context_data(**kwargs)
        member = get_member(self.request.user)
        context['role'] = member.role
        context['notify'] = Notification.objects.filter()

        return context


class editorsChief(TemplateView):
    second_model = Book
    template_name = 'books/editor/libros_publicados.html'

    def get_context_data(self, **kwargs):
        context = super(editorsChief, self).get_context_data(**kwargs)
        member = get_member(self.request.user)
        context['role'] = member.role

        return context

class notifyEs(TemplateView):
    model = Notification
    template_name = 'books/escritor/notificaciones.html'

    def get_context_data(self, **kwargs):
        context = super(notifyEs, self).get_context_data(**kwargs)
        member = get_member(self.request.user)
        context['notify'] = Notification.objects.filter()

        return context

class notifyEd(TemplateView):
    model = Notification
    template_name = 'books/editor/notificaciones.html'

    def get_context_data(self, **kwargs):
        context = super(notifyEd, self).get_context_data(**kwargs)
        member = get_member(self.request.user)
        context['role'] = member.role
        context['notify'] = Notification.objects.filter()

        return context

class notifyDis(TemplateView):
    model = Notification
    template_name = 'books/diseñador/notificaciones.html'

    def get_context_data(self, **kwargs):
        context = super(notifyEd, self).get_context_data(**kwargs)
        member = get_member(self.request.user)
        context['notify'] = Notification.objects.filter()

        return context


class disenyChief(TemplateView):
    second_model = Book
    template_name = 'books/diseñador/disenyo_asig.html'

    def get_context_data(self, **kwargs):
        context = super(disenyChief, self).get_context_data(**kwargs)
        member = get_member(self.request.user)
        context['role'] = member.role

        return context