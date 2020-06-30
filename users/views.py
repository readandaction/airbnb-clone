from django.shortcuts import render
from django.views import View


class LoginView(View):
    """ LoginView Definition """

    def get(self, request):
        return render(request, "users/login.html")

    def post(self, request):
        pass


# def login(request):
#     if request.GET.method == "get":
#     else request.GET.method == "post":
