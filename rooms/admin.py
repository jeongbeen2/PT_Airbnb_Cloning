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

    fieldsets = (
        (
            "Spaces",
            {
                "fields": (
                    "beds",
                    "bedrooms",
                    "baths",
                )
            },
        ),
        (
            "Basic Info",
            {
                "fields": (
                    "name",
                    "description",
                    "country",
                    "address",
                    "price",
                ),
            },
        ),
        (
            "Times",
            {
                "fields": (
                    "check_in",
                    "check_out",
                    "instant_book",
                )
            },
        ),
        (
            "More About the Space",
            {
                "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rules"),
            },
        ),
        ("last Details", {"fields": ("host",)}),
    )
    """ fieldset 내에서, fields, classes 등 다양한 기능이 있다. """
    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
    )
    """ #6.2 => ordering으로, 내가 지정해서 정렬해줄수도 있다. """
    ordering = (
        "name",
        "price",
    )
    """#6.1 => ForeignKey값을 가지고 오고 싶다면, __를 이용해 하부내용까지 가져와야 한다.  """

    list_filter = (
        "instant_book",
        "host__superhost",
        "country",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
    )
    """ #6.0 => Admin Panel에 search 기능을 추가하고 싶다면, 아래와 같이하자. """
    """ ^city, =city, @city ... """
    search_fields = ("city", "host__gender", "^host__username")

    """ #6.1 => filter_horizontal 은 Many to many field에서만 사용가능. """
    """ 내용물들을 검색하고, 삭제할수 있고 등등. """

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )

    """ #6.2 => many to many를 list에 넣어주기 위해서는, 그냥 list에 amenities만 넣어주면 오류발생. """
    """ def __str__ 처럼, def count_amenities라는 함수를 새로 만들어서 지정해 줘야 한다. """
    """ list_display에 count_amenities 입력 후, def 지정. """

    def count_amenities(self, obj):
        return obj.amenities.count()


@admin.register(models.Photo)
class PhotoADmin(admin.ModelAdmin):
    """ Photo Admin Definition """

    pass