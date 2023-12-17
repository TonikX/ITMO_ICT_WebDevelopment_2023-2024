from django import forms
from .models import Profile, Homework, SubmittedHomework
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django.utils import timezone 

class PostHomework(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ('subject', 'body', 'end_date', 'student_class', 'subject')

        widgets = {
            'subject': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'end_date': DateTimePickerInput(
                attrs={'class': 'form-control'},
                options={
                    'format': 'DD-MM-YYYY HH:mm',
                    'showTodayButton': True,
                    'minDate': timezone.now().strftime('%Y-%m-%d %H:%M'),
                }
            ),
            'student_class': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Remove 'user' from kwargs
        super().__init__(*args, **kwargs)
        student_classes = Profile.objects.filter(role='student').values_list('student_class', flat=True).distinct()
        class_choices = [(cls, cls) for cls in student_classes]
        class_choices.insert(0, ('', 'Choose a class'))
        self.fields['student_class'].widget.choices = class_choices
        if user and user.profile.role == 'teacher':
            allowed_subjects = user.profile.subjects.all().distinct()
            allowed_subjects = [(cls.name, cls.name) for cls in allowed_subjects]
            allowed_subjects.insert(0, ('', 'Choose a subject'))
            self.fields['subject'].widget.choices = allowed_subjects

class EditHomework(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ('body', 'end_date', 'student_class')

        widgets = {
                'body': forms.Textarea(attrs={'class': 'form-control'}),
                'end_date': DateTimePickerInput(
                    attrs={'class': 'form-control'},
                    options={
                        'format': 'DD-MM-YYYY HH:mm',
                        'showTodayButton': True,
                        'minDate': timezone.now().strftime('%Y-%m-%d %H:%M'),
                    }
                ),
                'student_class': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        student_classes = Profile.objects.filter(role='student').values_list('student_class', flat=True).distinct()
        class_choices = [(cls, cls) for cls in student_classes]
        self.fields['student_class'].widget.choices = class_choices

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = SubmittedHomework
        fields = ('homework_body',)
        widgets = {
            'homework_body': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }