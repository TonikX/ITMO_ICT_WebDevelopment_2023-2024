from django import forms

from race.models import Comment


class RaceRegistrationForm(forms.Form):
    team_name = forms.CharField(max_length=100)
    car_description = forms.CharField(widget=forms.Textarea)
    experience = forms.IntegerField(
        widget=forms.NumberInput(attrs={'placeholder': 'years'})
    )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_content', 'comment_type', 'rating']