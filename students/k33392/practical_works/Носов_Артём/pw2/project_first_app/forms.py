from django import forms
from .models import ExampleModel
  
  
# creating a form
class ExampleForm(forms.ModelForm):
  
    # create meta class
    class Meta:
        # specify model to be used
        model = ExampleModel
  
        # specify fields to be used
        fields = [
            "title",
            "description",
        ]