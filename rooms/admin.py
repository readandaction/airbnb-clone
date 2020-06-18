from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition"""

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    fieldsets = (
        (
            "Basic info",
            {"fields": ("name", "description", "country", "city", "price", "adress",)},
        ),
        ("Spaces", {"fields": ("beds", "bedrooms", "baths",)},),
        ("Time", {"fields": ("check_in", "check_out", "instant_book",)},),
        (
            "More about Spaces",
            {
                "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rules",),
            },
        ),
        ("Last Detail", {"fields": ("host",)}),
    )

    list_display = (
        "name",
        "price",
        "country",
        "city",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "count_amenities",
    )

    list_filter = (
        "instant_book",
        "host__superhost",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",
    )
    ordering = (
        "name",
        "price",
        "beds",
    )

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )

    search_fields = ("=city", "host__username")

    def count_amenities(self, obj):
        print(obj)
        print(obj.amenities)
        print(obj.amenities.all())
        return "potato"

    count_amenities.short_description = "Hellow"


@admin.register(models.Photho)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    pass
