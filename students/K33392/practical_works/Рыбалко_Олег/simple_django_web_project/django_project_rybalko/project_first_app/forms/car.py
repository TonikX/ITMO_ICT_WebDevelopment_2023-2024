from django.forms import ModelForm
from project_first_app.models import CarOwner

class CarModelForm(ModelForm):
    class Meta:
        model = CarOwner
        fields = [
            "name",
            "surname",
            "date_of_birth"
        ]
    