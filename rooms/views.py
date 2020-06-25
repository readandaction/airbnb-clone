from django.views.generic import ListView
from . import models

# Create your views here.


class HomeView(ListView):

    """ Home View Defintion """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "price"
