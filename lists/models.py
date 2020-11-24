from django.db import models
from core import models as core_models


class List(core_models.TimeStampedModel):
    """ List Model Definition """

    name = models.CharField(max_length=80)
    user = models.ForeignKey(
        "users.User", related_name="lists", on_delete=models.CASCADE
    )
    room = models.ManyToManyField("rooms.Room", related_name="lists", blank=True)
    """ rooms -> room으로 입력, 그러나 어디서부터 잘못된지 몰라서 수정못하고있음 ㅜ.ㅜ """

    def __str__(self):
        return self.name

    def count_rooms(self):
        return self.room.count()

    count_rooms.short_description = "Number of Rooms"