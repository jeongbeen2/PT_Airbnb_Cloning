from rooms.models import Room
from django.contrib import admin
from django.contrib.admin.decorators import register
from django.contrib.auth.admin import UserAdmin
from . import models
from rooms import models as room_models

""" #8.6 >> rooms의 모델을 받아와서, user 안에 Inline을 만들어줬다. """


class RoomInline(admin.TabularInline):

    model = room_models.Room


@admin.register(models.User)  # Decorator
class CustomUserAdmin(UserAdmin):
    """ Custom User Admin """

    inlines = (RoomInline,)

    fieldsets = UserAdmin.fieldsets + (
        (
            "NewBox",
            {
                "fields": (
                    "Bio",
                    "avatar",
                    "gender",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                ),
            },
        ),
    )
    list_filter = UserAdmin.list_filter + ("superhost",)
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
    )


# admin.site.register(models.User, UserAdmin)
# @admin.register(models.User) 와 똑같음.