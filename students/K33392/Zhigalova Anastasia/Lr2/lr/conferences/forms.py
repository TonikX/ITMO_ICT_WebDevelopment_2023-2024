from django import forms
from .models import Presentation, Registration, Review, Conference

class PresentationForm(forms.ModelForm):
    class Meta:
        model = Presentation
        fields = ['title', 'abstract']  

    def __init__(self, *args, **kwargs):
        super(PresentationForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['abstract'].widget.attrs.update({'class': 'form-control'})

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['conference', 'title'] 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [ 'text', 'rating']
        widgets = {
            'text': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
            'rating': forms.Select(choices=Review._meta.get_field('rating').choices),
        }

    