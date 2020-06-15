from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here


class User(AbstractUser):
    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_KOR = "kr"
    LANGUAGE_EN = "en"

    LANGUAGE_CHOICES = ((LANGUAGE_KOR, "Kr"), (LANGUAGE_EN, "En"))

    CURRENCY_KOREAN = "kwr"
    CURRENCY_USD = "usd"
    CURRENCY_CHOICES = ((CURRENCY_KOREAN, "KWR"), (CURRENCY_USD, "USD"))
    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, null=True, max_length=10)
    bio = models.TextField(default="")
    birthdate = models.DateField(null=True)
    langauge = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=2, null=True, blank=True
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=3, null=True, blank=True
    )
    superhost = models.BooleanField(default=False)
