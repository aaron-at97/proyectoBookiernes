from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import FormView
from eBook.views import get_member
from eBook.forms import LoginForm


class LoginView(FormView):
    """
    Clase que gestiona el formulario de inicio de sesión.
    """
    template_name = 'auth/staff_login.html'
    form_class = LoginForm

    def form_valid(self, form):
        """
        Método gestiona la validación de los datos enviados en el formulario.
        """
        usuario = form.cleaned_data['username']
        contrasena = form.cleaned_data['password']
        usuario = authenticate(username=usuario, password=contrasena)
        login(self.request, usuario)
        return HttpResponseRedirect(get_member(usuario).get_homepage())