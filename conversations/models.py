import conversations
from django.db import models
from core import models as core_models


class Conversation(core_models.TimeStampedModel):
    """ Conversation Model Definition """

    participants = models.ManyToManyField("users.User", blank=True)

    def __str__(self):
        usernames = []
        for user in self.participants.all():
            usernames.append(user.username)
        return ", ".join(usernames)

    """ " ".join Method는, list에 있는 값들을 앞에 "" 안에있는 것으로 구분하여 str형태로 가져온다. """

    def count_messages(self):
        return self.messages.count()

    count_messages.short_description = "Number of Messages"
    """ #8.2 >> count_messages는, Conversation에는 없는 항목이다. 그러나, 아래 Message class에서 ForeignKey로, related_name = "messages"로 """
    """ 가져 왔기 때문에, self.messages 의 항목으로 담길 수 있는 것임. """
    """ 주의사항 ==> 불러올때는, 꼭 related_name으로 가져온 것을 불러와야함. """

    def count_participants(self):
        return self.participants.count()

    count_participants.short_description = "Number of Participants"


class Message(core_models.TimeStampedModel):

    message = models.TextField()
    user = models.ForeignKey(
        "users.User", related_name="messages", on_delete=models.CASCADE
    )
    conversation = models.ForeignKey(
        "Conversation", related_name="messages", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user} says : {self.message}"