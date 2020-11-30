from django.db import models
from django_countries.fields import CountryField
from core import models as core_models


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
    """ Meta class의 자세한 사용법은 https://docs.djangoproject.com/en/3.1/ref/models/options/ """

    class Meta:
        verbose_name_plural = "Room Type"
        # ordering = ["name"]


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


class Photo(core_models.TimeStampedModel):
    """ Photo Moedl Definition """

    caption = models.CharField(max_length=80)

    """ ImageField는 upload_to를 통하여, 어느 폴더에 저장될 것인지를 지정할 수 있다. """
    file = models.ImageField(upload_to="room_photos")

    room = models.ForeignKey("Room", related_name="photos", on_delete=models.CASCADE)
    """ ForeignKey를 해줄 때, 첫번째 파라미터는 class를 가져와야 한다. ex. Room.. """
    """ 이때, Photo는 Room을 가져와야 하는데, 파이썬은 수직으로 파일을 읽기 때문에 room보다 아래에 있어야한다. """
    """ Room값을 "Room", 즉 String값으로 변경시켜주면 파일 전체에서 찾아오기 때문에, 에러가 나지 않는다. """
    """ Room -> (X), "Room" -> (O) """

    def __str__(self):
        return self.caption


class Room(core_models.TimeStampedModel):
    """ Room Model Definition """

    name = models.CharField(max_length=140, null=True)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.PositiveIntegerField()
    address = models.CharField(max_length=140, blank=True)
    guests = models.PositiveIntegerField()
    beds = models.PositiveIntegerField()
    bedrooms = models.PositiveIntegerField()
    baths = models.PositiveIntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    """ user_models.User => users.User """
    host = models.ForeignKey(
        "users.User", related_name="rooms", on_delete=models.CASCADE
    )
    """ #4.4 => room_type은 한 유형의 객실만 가져야 하고 싶으므로, ForeignKey를 사용하고, Roomtype를 제거해도 다른것에 영향이없게 """
    """ on_delete = SET_NULL을 해주는 것이다. """
    room_type = models.ForeignKey(
        "RoomType",
        related_name="rooms",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    amenities = models.ManyToManyField("Amenity", related_name="rooms", blank=True)
    facilities = models.ManyToManyField("Facility", related_name="rooms", blank=True)
    house_rules = models.ManyToManyField("HouseRule", related_name="rooms", blank=True)

    def __str__(self):
        return self.name

    """ #8.8 >> save를 interception해서 우리가 원하는대로 바꿔주고, ex) self.city = 'potato'하면 저장해도 potato로 바뀜 """
    """ 그다음 super().save(*args, **kwargs)를 해주면 원상태로 잘 저장된다. """

    """ 저장할때 앞에 대문자를 주고싶어서 시작했고, 이를 저장할때 intercept를 통해서 대문자로 바꿔주고, 다시 원래 부모 클래스를 불러와서 저장함. """

    def save(self, *args, **kwargs):
        self.city = str.capitalize(self.city)
        super().save(*args, **kwargs)

    """ #9.3>> division by zero errer -> 방을 만들었을 때, 방 리뷰가 0점인 것을 방지하려고 if문을 붙임. """

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        if len(all_reviews) > 0:
            for review in all_reviews:
                all_ratings += review.rating_average()
            return all_ratings / len(all_reviews)
        return 0
