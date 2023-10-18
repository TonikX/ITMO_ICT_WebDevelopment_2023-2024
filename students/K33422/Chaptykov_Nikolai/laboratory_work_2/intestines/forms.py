from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Student, SchoolGroup
from django.shortcuts import get_object_or_404


class UserCreateForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    group = forms.ModelMultipleChoiceField(
                        queryset=SchoolGroup.objects.all(),
                        label="School group",
                        widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'group', 'username']

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=True)
        group = f"{self.cleaned_data['group'].values_list('grade')[0][0]}{self.cleaned_data['group'].values_list('letter_id')[0][0]}"
        grade = group[0] if len(group) == 2 else group[0:1]
        letter = group[-1]
        student_object = Student(
        	user=user,
        	first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            group=get_object_or_404(SchoolGroup, letter_id=letter, grade=grade))
        student_object.save()
        return user, student_object