from django import forms
from .models import *

class HireStaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['name', 'surname', 'position']

    def __init__(self, *args, **kwargs):
        super(HireStaffForm, self).__init__(*args, **kwargs)
        self.fields['position'].widget = forms.Select(choices=Staff.POSITION_CHOICES)

class FireStaffForm(forms.Form):
    staff_id = forms.ModelChoiceField(queryset=Staff.objects.all(), label='Выберите служащего')

class AddCleaningForm(forms.ModelForm):
    class Meta:
        model = Cleaning
        fields = ['staff_id', 'room_id', 'date_clean']

class DeleteCleaningForm(forms.Form):
    cleaning = forms.ModelChoiceField(queryset=Cleaning.objects.all(), label='Select Cleaning')

class CheckinForm(forms.ModelForm):
    class Meta:
        model = Checkin
        fields = ['guest_id', 'room_id', 'check_in_date', 'check_out_date', 'staff_id']

class CheckoutForm(forms.Form):
    checkin = forms.ModelChoiceField(queryset=Checkin.objects.all(), label='Checkin')

class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['name', 'surname', 'passport_number', 'hometown', 'birth_date']

