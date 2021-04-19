from django import forms
from phone_field import PhoneField
from .models import Ngos

class NgoForm(forms.ModelForm):
    class Meta:
        model = Ngos
        exclude = ['account']