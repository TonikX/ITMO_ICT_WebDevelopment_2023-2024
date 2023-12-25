from django import forms
from .models import SubmittedWork

class SubmittedWorkForm(forms.ModelForm):
    class Meta:
        model = SubmittedWork
        fields = ['text']