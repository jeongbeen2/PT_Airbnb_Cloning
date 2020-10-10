from rooms.models import Amenity, Facility, HouseRule
from django.contrib import admin
from . import models


@admin.register(models.RoomType, Amenity, Facility, HouseRule)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    pass