from django.shortcuts import render
from django.views import View
from . import forms


class LoginView(View):
    """ LoginView Definition """

    def get(self, request):
        form = forms.LoginForm(initial={"email": "hswanson@smith.com"})
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        return render(request, "users/login.html", {"form": form})


# def login(request):
#     if request.GET.method == "get":
#     else request.GET.method == "post":
