from django.contrib import admin
from . import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    add_fieldsets = (
        (
            "NewBox",
            {
                "fields": ("Bio",),
            },
        ),
    )