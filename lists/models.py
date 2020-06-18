from django.db import models
from core import models as core_models


class List(core_models.TimeStampedModel):

    """ List Model Definition"""

    name = models.CharField(max_length=40)
    user = models.ForeignKey(
        "users.User", related_name="lists", on_delete=models.CASCADE
    )
    rooms = models.ManyToManyField("rooms.Room")

    def __str__(self):
        return self.name