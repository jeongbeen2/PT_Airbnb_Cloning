from django.db import models
from django.db.models.deletion import CASCADE
from core import models as core_models


class Review(core_models.TimeStampedModel):
    """ Review Model Definitions """

    review = models.TextField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", related_name="reviews", on_delete=models.CASCADE
    )

    def __str__(self):
        """ ForeignKey를 정의하면, 정의한 값 내에있는 값도 가져올 수 있음. """
        """ ex) self.room.city """
        """ ex2) self.room.host.username """
        """ 만일, 부르려는 값의 __str__값이 정의되어있으면 그값을 가져온다. """
        return f"{self.room} => {self.user} says : {self.review}"

    def rating_average(self):
        avg = (
            self.accuracy
            + self.communication
            + self.cleanliness
            + self.location
            + self.check_in
            + self.value
        ) / 6
        return round(avg, 2)

    """ 항목의 이름을 바꿔주고싶다면 이렇게하면 된다. """
    # rating_average.short_description = "oh my zsh"
