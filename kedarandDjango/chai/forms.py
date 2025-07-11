from django import forms
from .models import ChaiVariety

class ChaiVarietyForm(forms.Form):
    chai_varity = forms.CharField()