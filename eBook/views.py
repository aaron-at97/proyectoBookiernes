import json
import sys
import os

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from urllib import request, parse

from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from Bookiernes.settings import BASE_DIR
from eBook.models import Editor, EditorChief, Writer, ChiefDesigner, Designer, CTO, Developer, Clients, Notification, \
    Book


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
    elif Clients.objects.filter(user=user).exists():
        return Clients.objects.get(user=user)
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
        context = super(notifyDis, self).get_context_data(**kwargs)
        member = get_member(self.request.user)
        context['notify'] = Notification.objects.filter()

        return context


class notifyMaq(TemplateView):
    model = Notification
    template_name = 'books/maquetador/notificaciones.html'

    def get_context_data(self, **kwargs):
        context = super(notifyMaq, self).get_context_data(**kwargs)
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


class LeerLibro(TemplateView):
    template_name = 'books/client/leer_libro.html'

    def get_context_data(self, **kwargs):
        context = super(LeerLibro, self).get_context_data(**kwargs)
        data, pagina, libro = self.read_file(self.kwargs['libropk'], self.kwargs['pagnum'])

        context['data'] = data
        context['anterior'] = int(pagina) - 1
        context['pagina'] = pagina
        context['siguiente'] = int(pagina) + 1
        context['libro'] = libro

        return context

    def read_file(self, libro, pagina):
        data = ""
        try:
            with open(os.path.join(BASE_DIR, 'static') + "/img/Libros/" + libro + "/" + pagina + ".txt", "r",
                      encoding='utf8') as file:
                # Strip lines
                data = file.read()
        except Exception as e:
            with open(os.path.join(BASE_DIR, 'static') + "/img/Libros/" + libro + "/" + pagina + ".txt", "r",
                      encoding='iso-8859-1') as file:
                # Strip lines
                data = file.read()
        return data, pagina, libro


def traducir(request):
    libro = request.GET.get("libro")
    idioma = request.GET.get("idioma")

    return render(request, 'books/editor/solicitud_traduccion2.html', {"libropk": libro, "pagnum": idioma})

class TraducirLibro(TemplateView):
    template_name = 'books/editor/solicitud_traduccion2.html'

    def get_context_data(self, **kwargs):
        context = super(TraducirLibro, self).get_context_data(**kwargs)
        data = self.read_file(self.kwargs['libropk'], self.kwargs['pagnum'])
        context['data'] = data

        return context

    def read_file(self, libro, idioma):
        data = ""
        try:
            with open(os.path.join(BASE_DIR, 'static') + "/img/Libros/" + libro + "/" + "1.txt", "r",
                      encoding='utf8') as file:
                # Strip lines
                data = file.read()
                data = self.translate(data, "es", idioma, "https://translate.astian.org/translate", libro)
        except Exception as e:
            with open(os.path.join(BASE_DIR, 'static') + "/img/Libros/" + libro + "/" + "1.txt", "r",
                      encoding='iso-8859-1') as file:
                # Strip lines
                data = file.read()
                data = self.translate(data, "es", idioma, "https://translate.astian.org/translate", libro)

        return data

    def translate(self, q, source, idioma, url, libro):
        """Connect to LibreTranslate API
        Args:
            q (str): The text to translate
            source (str): The source language code (ISO 639)
            target (str): The target language code (ISO 639)

        Returns: The translated text
        """
        params = {"q": q, "source": source, "target": idioma}

        url_params = parse.urlencode(params)

        req = request.Request(url, data=url_params.encode())

        try:
            response = request.urlopen(req)
        except Exception as e:
            print(e, sys.stderr)
            return None

        try:
            response_str = response.read().decode()
        except Exception as e:
            print(e, sys.stderr)
            return None

        data = ""
        data = str(json.loads(response_str))
        nueva = ""
        ant = ""
        data = data[20:len(data)-2]

        for c in data:
            if c == '\\':
                nueva = nueva + " \n "
            elif ant == '\\':
                pass
            else:
                nueva = nueva + c
            ant = c
        try:
            with open(os.path.join(BASE_DIR, 'static') + "/img/Libros/" + libro + "/" + idioma + "/1.txt", 'w',
                      encoding='utf8') as file_write:
                # write json data into file
                file_write.write(nueva)
                file_write.close()

        except Exception as e:
            with open(os.path.join(BASE_DIR, 'static') + "/img/Libros/" + libro + "/" + idioma + "/1.txt", 'w',
                      encoding='iso-8859-1') as file_write:
                # Strip lines
                # write json data into file
                file_write.write(nueva)
                file_write.close()

        return data



class Verdemo(TemplateView):
    template_name = 'home/ver_demo.html'

    def get_context_data(self, **kwargs):
        context = super(Verdemo, self).get_context_data(**kwargs)
        data, libro = self.read_file(self.kwargs['libropk'], "1")

        context['data'] = data
        context['libro'] = libro
        context['autor'] = self.kwargs['autor']

        return context

    def read_file(self, libro, pagina):
        data = ""
        try:
            with open(os.path.join(BASE_DIR, 'static') + "/img/Libros/" + libro + "/" + pagina + ".txt", "r",
                      encoding='utf8') as file:
                # Strip lines
                data = file.read()
        except Exception as e:
            with open(os.path.join(BASE_DIR, 'static') + "/img/Libros/" + libro + "/" + pagina + ".txt", "r",
                      encoding='iso-8859-1') as file:
                # Strip lines
                data = file.read()
        return data, libro
