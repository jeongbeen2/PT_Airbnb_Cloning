from django.db import models


class TimeStampedModel(models.Model):
    """ Time Stamped Model """

    """ auto_now_add => model이 생성된 시간을 저장, auto_now => 새로운 날짜로 계속 업데이트. """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    """ Meta Class => 데이터베이스에 들어가는 것을 원하지 않을 때. """

    class Meta:
        abstract = True