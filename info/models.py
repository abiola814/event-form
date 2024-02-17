# myapp/models.py
from django.db import models
from django.utils.crypto import get_random_string

class EventAttendee(models.Model):
    fullName = models.CharField(("name"), max_length=50, help_text="name of attendee")
    email = models.EmailField(("email"), max_length=254)
    phone = models.CharField(("phone"), max_length=50)
    invitee = models.CharField(("invitee"), max_length=50)
    unique_id = models.CharField(max_length=10, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.unique_id:
            self.unique_id = get_random_string(length=10)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.fullName
