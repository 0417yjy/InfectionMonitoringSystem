# forms.py

from django import forms
from .models import Subscriber

class SubscirberForm(forms.Form):
    cCHOICES = (('a','a'),
               ('b','b'),
               ('c','c'),
               ('d','d'),)
    picked = forms.MultipleChoiceField(choices=CHOICES, widget=forms.CheckboxSelectMultiple())
