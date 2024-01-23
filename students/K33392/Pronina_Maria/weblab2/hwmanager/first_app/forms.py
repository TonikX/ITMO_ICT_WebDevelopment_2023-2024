from django import forms
from .models import Teacher, Solution


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            "username",
            "password",
            "last_name",
            "first_name",
            "second_name",
        ]


class StudentForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            "username",
            "password",
            "last_name",
            "first_name",
            "second_name",
        ]


class SolutionForm(forms.ModelForm):
    class Meta:
        model = Solution
        fields = [
            "student",
            "solution_text",
        ]
