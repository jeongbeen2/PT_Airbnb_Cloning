from rooms.models import Amenity, Facility, HouseRule
from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.RoomType, Amenity, Facility, HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """ Item Admin Definition """

    list_display = (
        "name",
        "used_by",
    )
    """#7.3 => room_type을 가진 모든 방의 갯수를 보여주고 싶으므로. 아래와같이 한다. """

    def used_by(self, obj):
        return obj.rooms.count()

    pass


""" #8.6>> Photo admin을, room의 admin 안에다가 넣는 방법 ==> Inline """
""" TabularInline / StackedInline으로, 보이는 것이 달라진다. """


class PhotoInline(admin.TabularInline):

    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """ Room Admin Definition """

    inlines = (PhotoInline,)

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
                    "city",
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
        "count_photos",
        "total_rating",
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

    raw_id_fields = ("host",)
    """ #8.6>> raw_id는, 리스트의 수가 많아질 경우 사용한다. """
    """ 각 리스트에 id를 매겨서 검색할 수 있게 함. """

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
    """ save_model은, 누군가가 저장을 할때 정보를 알 수 있게 해주는 모델이고, 여러 admin을 관리할 때 유용하다. """
    # def save_model(self, request, obj, form, change):
    #     print(obj, change, form)
    #     super().save_model(request, obj, form, change)

    """ #6.2 => many to many를 list에 넣어주기 위해서는, 그냥 list에 amenities만 넣어주면 오류발생. """
    """ def __str__ 처럼, def count_amenities라는 함수를 새로 만들어서 지정해 줘야 한다. """
    """ list_display에 count_amenities 입력 후, def 지정. """

    def count_amenities(self, obj):
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()
        """ photos는 models.py > class photo > room > related_name = "photos" 연결. """


@admin.register(models.Photo)
class PhotoADmin(admin.ModelAdmin):
    """ Photo Admin Definition """

    list_display = (
        "__str__",
        "get_thumbnail",
    )
    """ #8.5 >> 썸네일은 admin에서만 보여질 것이기 때문에, admin에 만든다. """

    """ obj.file.url, obj.file.path 처럼, obj 안에는 수많은 정보가 있다. """

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"

    """ #8.5 정리>> photo 어드민패널 작업. """
    """ dir, var을 이용하여 obj의 클래스내용을 다 볼수있고, 파일이 가진 것을 볼 수 있다. """
    """ 그리고 f'<img width="50px" src="{obj.file.url}" />' 처럼, html 내부를 보려했지만 """
    """ 장고는 그것을 보안상 막아버린다. 그래서 mark_safe를 이용하여 장고한테 ㄱㅊ하다고 말해준다. """