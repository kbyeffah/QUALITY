from django.shortcuts import render
from django.http import HttpResponse
from .models import product
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


def home(request):
    context = {"key": "I am at Home "}
    return render(request, "Fproj/templates/Fproj/home.html", context)


class CustomLoginView(LoginView):
    template_name = "Fproj/login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        if User.is_staff or User.is_superuser:
            return reverse_lazy("admin")
        else:
            return reverse_lazy('')
