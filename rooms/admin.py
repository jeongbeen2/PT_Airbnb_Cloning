from rooms.models import Amenity, Facility, HouseRule
from django.contrib import admin
from . import models


@admin.register(models.RoomType, Amenity, Facility, HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """ Item Admin Definition """

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """ Room Admin Definition """

    pass


@admin.register(models.Photo)
class PhotoADmin(admin.ModelAdmin):
    """ Photo Admin Definition """

    pass