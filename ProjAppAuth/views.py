from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from ProjAppAuth.forms import UserRegisterForm
from django.views.generic import ListView, FormView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm

from ProjAppAuth.models import User


class UserRegister(FormView):
    form_class = UserRegisterForm
    template_name = "registration/register-v2.html"
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UserLoginView(LoginView):
    success_url = reverse_lazy("index")
    login_url = "index"
    template_name = "registration/login.html"


class UserLogoutView(LogoutView):
    next_page = reverse_lazy("login")


class UserPasswordChange(PasswordChangeView):
    form_class = PasswordChangeForm
    model = User
    template_name = "registration/password-change.html"
