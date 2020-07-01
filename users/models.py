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

    LANGUAGE_CHOICES = ((LANGUAGE_KOR, "Korea"), (LANGUAGE_EN, "English"))

    CURRENCY_KOREAN = "kwr"
    CURRENCY_USD = "usd"
    CURRENCY_CHOICES = ((CURRENCY_KOREAN, "KWR"), (CURRENCY_USD, "USD"))
    avatar = models.ImageField(blank=True, upload_to="avatars")
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(blank=True)
    birthdate = models.DateField(null=True, blank=True)
    langauge = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=2, blank=True, default=LANGUAGE_KOR
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=3, blank=True, default=CURRENCY_KOREAN
    )
    superhost = models.BooleanField(default=False)
    email_confirmed = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=120, default="", blank=True)

    def verify_email(self):
        pass
