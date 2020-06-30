from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.views import View
from . import forms


class LoginView(View):
    """ LoginView Definition """

    def get(self, request):
        form = forms.LoginForm(initial={"email": "read@gmail.com"})
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("core:home"))

        return render(request, "users/login.html", {"form": form})


def log_out(request):
    """ logout definition"""
    logout(request)
    return redirect(reverse("users:login"))


# def login(request):
#     if request.GET.method == "get":
#     else request.GET.method == "post":
