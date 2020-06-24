from datetime import datetime
from django.shortcuts import render
from . import models

# Create your views here.


def all_rooms(request):
    now = datetime.now()
    all_rooms = models.Room.objects.all()
    return render(request, "rooms/home.html", context={"now": now, "rooms": all_rooms})

