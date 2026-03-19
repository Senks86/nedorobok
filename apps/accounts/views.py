from django.shortcuts import render

from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "home.html"

from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import SignUpForm

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "signup.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

from django.contrib.auth.mixins import LoginRequiredMixin

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "profile.html"

class AboutView(TemplateView):
    template_name = "about.html"

class NotificationView(TemplateView):
    template_name = "notifications.html"


