from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class CustomUser(AbstractUser):
    # first_name and last_name do not cover global name patterns
    name = models.CharField("Name of User", blank=True, max_length=255)
    bio = models.TextField("Bio", blank=True)

    def get_absolute_url(self):
        return reverse("user_detail", kwargs={"username": self.username})
