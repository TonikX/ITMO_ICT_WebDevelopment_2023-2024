from django import forms
from .models import Reservation, Review


class ReserveForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['tour']
        widgets = {
            'tour': forms.Textarea(attrs={'rows':2, 'cols':25}),
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'rating']
        widgets = {
            'text': forms.Textarea(attrs={'rows':3, 'cols':25}),
            'rating': forms.Select(choices=[(i, i) for i in range(1, 11)]),
        }

