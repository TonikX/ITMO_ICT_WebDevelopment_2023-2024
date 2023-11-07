from django import forms
from .models import Owner, Car

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['surname', 'name', 'birthday_date']


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'  # Включить все поля модели

class CarDeleteByIdForm(forms.Form):
    car_id = forms.IntegerField(
        required=True,
        label='ID автомобиля для удаления',
    )
