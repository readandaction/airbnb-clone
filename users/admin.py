from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from rooms import models as rooms_models

# Register your models here.
class RoomInline(admin.TabularInline):
    model = rooms_models.Room


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    """ Custom User Admin"""

    inlines = (RoomInline,)

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom User info",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "langauge",
                    "currency",
                    "superhost",
                )
            },
        ),
    )

    list_filter = UserAdmin.list_filter + ("superhost",)

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "langauge",
        "currency",
        "superhost",
        "is_staff",
        "is_active",
        "is_superuser",
    )
