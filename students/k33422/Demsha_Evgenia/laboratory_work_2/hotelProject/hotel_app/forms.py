from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Booking, Comment
import datetime


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		if commit:
			user.save()
		return user


class BookRoomForm(forms.ModelForm):

	class Meta:
		model = Booking
		fields = ("date_start", "date_end")

	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop('user', None)
		self.room = kwargs.pop('room', None)
		super(BookRoomForm, self).__init__(*args, **kwargs)

	date_start = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
	date_end = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

	def save(self, commit=True):
		booking = super(BookRoomForm, self).save(commit=False)
		booking.user = self.user
		booking.room = self.room
		if commit:
			booking.save()
		return booking


class ReviewForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ("rating", "content")

	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop('user', None)
		self.room = kwargs.pop('room', None)
		super(ReviewForm, self).__init__(*args, **kwargs)

	def save(self, commit=True):
		comment = super(ReviewForm, self).save(commit=False)
		comment.user = self.user
		comment.room = self.room
		comment.date = datetime.date.today()
		if commit:
			comment.save()
		return comment
