from django.shortcuts import render
from django.views import View
from . import forms


class LoginView(View):
    """ LoginView Definition """

    def get(self, request):
        form = forms.LoginForm()
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        print(form)


# def login(request):
#     if request.GET.method == "get":
#     else request.GET.method == "post":
