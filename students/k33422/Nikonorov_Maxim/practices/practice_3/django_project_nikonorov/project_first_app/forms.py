from django import forms
from .models import CarOwner, Car
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django.utils import timezone 

class NewOwner(forms.ModelForm):
    class Meta:
        model = CarOwner
        fields = ('username', 'password', 'FirstName', 'LastName', 'DateOfBirth', 'PassportNumber', 'Address', 'Nationality')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
            'FirstName': forms.TextInput(attrs={'class': 'form-control'}),
            'LastName': forms.TextInput(attrs={'class': 'form-control'}),
            'DateOfBirth': DateTimePickerInput(
                attrs={'class': 'form-control'},
                options={
                    'format': 'DD-MM-YYYY',
                    'showTodayButton': True,

                }
            ),
            'PassportNumber': forms.TextInput(attrs={'class': 'form-control'}),
            'Address': forms.TextInput(attrs={'class': 'form-control'}),
            'Nationality': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
class NewCar(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('Number', 'Brand', 'Model', 'Colour')

        widgets = {
            'Number': forms.TextInput(attrs={'class': 'form-control'}),
            'Brand': forms.TextInput(attrs={'class': 'form-control'}),
            'Model': forms.TextInput(attrs={'class': 'form-control'}),
            'Colour': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
class EditCar(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('Number', 'Colour')

        widgets = {
            'Number': forms.TextInput(attrs={'class': 'form-control'}),
            'Colour': forms.TextInput(attrs={'class': 'form-control'}),
        }