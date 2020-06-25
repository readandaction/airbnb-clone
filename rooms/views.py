from math import ceil
from datetime import datetime
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models

# Create your views here.


def all_rooms(request):
    page = request.GET.get("page", 1)
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10)
    rooms = paginator.get_page(page)
    return render(request, "rooms/home.html", context={"page": rooms},)

