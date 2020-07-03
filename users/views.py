import os
import requests
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.views import View
from . import forms, models


class LoginView(FormView):
    """ LoginView Definition """

    template_name = "users/login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
            return redirect(reverse("core:home"))

        return super().form_valid(form)


# class LoginView(View):
#     """ LoginView Definition """

#     def get(self, request):
#         form = forms.LoginForm(initial={"email": "read@gmail.com"})
#         return render(request, "users/login.html", {"form": form})

#     def post(self, request):
#         form = forms.LoginForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data.get("email")
#             password = form.cleaned_data.get("password")
#             user = authenticate(request, username=email, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect(reverse("core:home"))

#         return render(request, "users/login.html", {"form": form})


def log_out(request):
    """ logout definition"""
    logout(request)
    return redirect(reverse("users:login"))


# def login(request):
#     if request.GET.method == "get":
#     else request.GET.method == "post":


class SignupView(FormView):
    """ SignupView Definition """

    template_name = "users/signup.html"
    form_class = forms.SignupForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        user.verify_email()
        return super().form_valid(form)


def complete_verification(request, key):
    try:
        user = models.User.objects.get(email_secret=key)
        user.email_secret = ""
        user.email_verified = True
        user.save()
        # to do : add success message
    except models.User.DoesNotExist:
        # to do : add error
        pass
    return redirect(reverse("core:home"))


def github_login(request):
    client_id = os.environ.get("GH_ID")
    redirect_uri = "http://127.0.0.1:8000/users/login/github/callback"
    return redirect(
        f"https://github.com/login/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&scope=read:user"
    )


def github_callback(request):
    client_id = os.environ.get("GH_ID")
    client_secret = os.environ.get("GH_SECRET")
    code = request.GET.get("code", None)
    if code is not None:
        request = requests.post(
            f"https://github.com/login/oauth/access_token?client_id={client_id}&client_secret={client_secret}&code={code}",
            header={"Accept": "application/json"},
        )
    else:
        return redirect(reverse("core:home")

