from django import forms
from main.models import comment


class commentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ("message",)
