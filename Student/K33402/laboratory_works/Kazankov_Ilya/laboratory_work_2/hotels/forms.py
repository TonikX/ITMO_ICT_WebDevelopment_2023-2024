from django.forms import ModelForm
from .models import Booking, Customer, Review
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BookingForm(ModelForm):
	class Meta:
		model = Booking
		fields = ['check_in_date', 'check_out_date']
		
class EditBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['check_in_date', 'check_out_date']
		
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'
		exclude = ['user']
            
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        exclude = ['booking']