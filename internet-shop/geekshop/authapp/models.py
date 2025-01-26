from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now


def get_activation_key_expiration_date():
    return now() + timedelta(days=2)


# Create your models here.
class ShopUser(AbstractUser):
    age = models.PositiveIntegerField(verbose_name="возраст")
    avatar = models.ImageField(verbose_name="аватар", blank=True, upload_to="users")
    phone = models.CharField(
        max_length=20,
        verbose_name="телефон",
        blank=True,
    )
    city = models.CharField(max_length=20, verbose_name="город", blank=True)
    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(
        default=get_activation_key_expiration_date
    )

    def is_activation_key_expired(self):
        if now() <= self.activation_key_expires:
            return False
        return True
