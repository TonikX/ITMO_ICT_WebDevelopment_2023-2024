from django.forms import ModelForm

from project_first_app.models import CarOwner


class CarOwnerModelForm(ModelForm):
    class Meta:
        model = CarOwner
        fields = [
            "first_name",
            "last_name",
            "username",
            "password",
            "date_of_birth",
            "passport_number",
            "home_address",
            "nationality",
        ]
