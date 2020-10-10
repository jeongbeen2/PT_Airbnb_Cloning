from django.contrib import admin
from django.contrib.admin.decorators import register
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)  # Decorator
class CustomUserAdmin(UserAdmin):
    """ Custom User Admin """

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

    list_display = ("username", "gender", "language", "currency", "superhost")
    list_filter = ("superhost",)


# admin.site.register(models.User, UserAdmin)
# @admin.register(models.User) 와 똑같음.