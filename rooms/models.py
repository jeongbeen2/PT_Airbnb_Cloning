from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models


class AbstractItem(core_models.TimeStampedModel):
    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    """ RoomType Model Definition """
    """ #4.5 => Meta class에서, verbose_name을 사용해 주면, 장고의 기본 복수형 출력값을 임의로 바꿔줄 수 있다. """
    class Meta:
        verbose_name_plural = "Room Type"


class Amenity(AbstractItem):
    """ Amenity Model Definition """

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):
    """ Facility Model Definition """

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):
    """ HouseRule Model Definition """

    class Meta:
        verbose_name_plural = "House Rule"


class Room(core_models.TimeStampedModel):
    """ Room Model Definition """

    name = models.CharField(max_length=140, null=True)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140, blank=True)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    """ #4.4 => room_type은 한 유형의 객실만 가져야 하고 싶으므로, ForeignKey를 사용하고, Roomtype를 삭제해도 다른것에 영향이없게
    on_delete = SET_NULL을 해주는 것이다. """
    room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField(Amenity)
    facilities = models.ManyToManyField(Facility)
    house_rules = models.ManyToManyField(HouseRule)

    def __str__(self):
        return self.name