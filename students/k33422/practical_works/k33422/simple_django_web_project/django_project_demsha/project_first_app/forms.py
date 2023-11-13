from project_first_app.models import User
from django import forms


class OwnerForm(forms.ModelForm):
  # create meta class
  class Meta:
    # specify model to be used
    model = User

    # specify fields to be used
    fields = [
      "last_name",
      "first_name",
      "birth_date",
      "passport",
      "address",
      "nationality",
    ]

