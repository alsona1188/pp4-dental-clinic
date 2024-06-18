from django import forms
from django.contrib.auth.models import User
from .models import ContactFormRequest


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactFormRequest
        fields = fields = ['email', 'subject', 'message']