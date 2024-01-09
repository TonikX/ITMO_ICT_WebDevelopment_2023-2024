from django import forms
from .models import Owner, Car, UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['passport_number', 'home_address', 'nationality']
class OwnerForm(forms.ModelForm):
    user_profile_form = UserProfileForm()

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
