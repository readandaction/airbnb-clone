from django.views.generic import ListView
from django.shortcuts import render
from . import models

# Create your views here.


class HomeView(ListView):

    """ Home View Defintion """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "price"
    context_object_name = "rooms"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def rooms_detail(request, pk):
    return render(request, "rooms/detail.html")
