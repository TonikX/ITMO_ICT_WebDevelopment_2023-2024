from django import forms
from .models import Answer

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer # на основе этой модели
        fields = ['answer_text', 'homework'] #поля