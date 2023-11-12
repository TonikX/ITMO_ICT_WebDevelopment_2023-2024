from django import forms
from .models import Presentation, Registration, Review, Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['username', 'password', 'first_name', 'last_name', 'occupation', 'is_admin']
        labels = {
            'username': 'username',
            'password': 'password',
            'first_name': 'name',
            'last_name': 'surname',
            'occupation': 'occupation',
            'is_admin': 'access status',
        }

class PresentationForm(forms.ModelForm):
    class Meta:
        model = Presentation
        fields = ['conference', 'author', 'title', 'approved_pres']
        labels = {
            'conference': 'conference',
            'author': 'assigned authors',
            'title': 'title',
            'approved_pres': 'approval status',
        }


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['author', 'conference', 'title', 'approved_reg']
        labels = {
            'author': 'conference',
            'conference': 'assigned authors',
            'title': 'title',
            'approved_reg': 'approval status',
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['comment_date']
        fields = ['conference', 'author', 'text', 'rating']
        labels = {
            'conference': 'conference',
            'author': 'author',
            'text': 'text',
            'rating': 'rating',
        }