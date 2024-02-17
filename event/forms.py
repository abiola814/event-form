# myapp/forms.py
from django import forms
from info.models import EventAttendee

class EventAttendeeForm(forms.ModelForm):
    class Meta:
        model = EventAttendee
        fields = ['fullName', 'email', 'phone', 'invitee', 'unique_id']
