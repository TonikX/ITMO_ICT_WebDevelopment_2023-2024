from django import forms
from .models import Car, CarOwner


class CarOwnerCreateForm(forms.ModelForm):
    class Meta:
        model = CarOwner
        fields = ["username", "password", "name", "surname", "birthday", 'nationality', 'passport', 'home_address']


class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ["state_number", "brand", "model", "color"]


class CarUpdateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ["state_number", "brand", "model", "color"]
