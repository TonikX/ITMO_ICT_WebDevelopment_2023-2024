from django import forms

from apps.homework.models import Submission, Grade


class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ('content', 'comments')


class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['value', 'comments']
