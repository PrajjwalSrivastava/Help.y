from django import forms
from phone_field import PhoneField
from .models import Organization


class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        exclude = ['account']

