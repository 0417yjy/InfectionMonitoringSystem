# forms.py

from django import forms
from .models import Subscriber

class SubscirberForm(forms.Form):
    class Meta:
        model = Subscriber
        fields = ['address']