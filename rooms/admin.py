from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """ Item Admin Definition"""

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    list_display = (
        "name",
        "country",
        "city",
        "guests",
        "beds",
        "bedrooms",
        "baths",
    )

    list_filter = ("instant_book", "city", "country")

    search_fields = ("=city", "host__username")


@admin.register(models.Photho)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    pass
