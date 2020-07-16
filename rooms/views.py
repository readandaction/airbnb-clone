from django.views.generic import ListView, DetailView, View, UpdateView
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django_countries import countries
from . import models, forms
from users import mixins as user_mixins

# Create your views here.


class HomeView(ListView):

    """ Home View Defintion """

    model = models.Room
    paginate_by = 12
    paginate_orphans = 5
    ordering = "price"
    context_object_name = "rooms"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# def room_detail(request, pk):
#     try:
#         room = models.Room.objects.get(pk=pk)
#         return render(request, "rooms/detail.html", {"room": room})
#     except models.Room.DoesNotExist:
#         raise Http404()
class RoomDetail(DetailView):
    """ RoomDetail Definition"""

    model = models.Room


class SearchView(View):
    """ SearchView Definition """

    def get(self, request):
        country = request.GET.get("country")
        if country:
            form = forms.SearchForm(request.GET)
            if form.is_valid():
                city = form.cleaned_data.get("city")
                country = form.cleaned_data.get("country")
                room_type = form.cleaned_data.get("room_type")
                price = form.cleaned_data.get("price")
                guests = form.cleaned_data.get("guests")
                beds = form.cleaned_data.get("beds")
                baths = form.cleaned_data.get("baths")
                bedrooms = form.cleaned_data.get("bedrooms")
                instant_book = form.cleaned_data.get("instant_book")
                superhost = form.cleaned_data.get("superhost")
                amenities = form.cleaned_data.get("amenities")
                facilities = form.cleaned_data.get("facilities")

                filter_args = {}
                if city != "Anywhere":
                    filter_args["city__startswith"] = city
                filter_args["country"] = country

                if room_type is not None:
                    filter_args["room_type"] = room_type

                if price is not None:
                    filter_args["price__lte"] = price
                if beds is not None:
                    filter_args["beds__gte"] = beds
                if guests is not None:
                    filter_args["guests__gte"] = guests
                if bedrooms is not None:
                    filter_args["bedrooms__gte"] = bedrooms
                if baths is not None:
                    filter_args["baths__gte"] = baths

                if instant_book is True:
                    filter_args["instant_book"] = True
                if superhost is True:
                    filter_args["host__superhost"] = True

                for amenity in amenities:
                    filter_args["amenities"] = amenity
                for facility in facilities:
                    filter_args["facilities"] = facility
                qs = models.Room.objects.filter(**filter_args).order_by("-created")

                paginator = Paginator(qs, 1, orphans=0)
                num_pages = paginator.num_pages
                page = request.GET.get("page", 1)
                rooms = paginator.page(page)
                return render(
                    request,
                    "rooms/search.html",
                    {
                        "form": form,
                        "rooms": rooms,
                        "page": page,
                        "num_pages": num_pages,
                    },
                )

        else:
            form = forms.SearchForm()

        return render(request, "rooms/search.html", {"form": form,},)


class EditRoomView(user_mixins.LogInRequiredView, UpdateView):
    model = models.Room
    fields = (
        "name",
        "description",
        "country",
        "city",
        "price",
        "adress",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
    )
    template_name = "rooms/room_edit.html"

    def get_object(self, queryset=None):
        room = super().get_object(queryset=queryset)
        if room.host != self.request.user:
            raise Http404()
        return room


class RoomPhotosView(user_mixins.LogInRequiredView, DetailView):

    model = models.Room
    template_name = "rooms/room_photos.html"

    def get_object(self, queryset=None):
        room = super().get_object(queryset=queryset)
        if room.host.pk != self.request.user.pk:
            raise Http404()
        return room


@login_required
def delete_photo(request, room_pk, photo_pk):
    user = request.user
    try:
        room = models.Room.objects.get(pk=room_pk)
        if user != room.host:
            messages.error(request, "Can't Delete that Photo")
        else:
            room.photos.filter(pk=photo_pk).delete()
        return redirect(reverse("rooms:photos", kwargs={"pk": room_pk}))
    except models.Room.DoesNotExist:
        return redirect(reverse("core:home"))


class EditPhotoView(user_mixins.LogInRequiredView, SuccessMessageMixin, UpdateView):

    model = models.Photo
    pk_url_kwarg = "photo_pk"
    template_name = "rooms/photo_edit.html"
    fields = ("caption",)
    success_message = "Photo Update"

    def get_success_url(self):
        room_pk = self.kwargs.get("room_pk")
        return reverse("rooms:photos", kwargs={"pk": room_pk})

