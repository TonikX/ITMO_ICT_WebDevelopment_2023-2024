## Forms

Форма регистрации посетителя конференции
```python
class UserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['birth_date'].widget = widgets.DateInput(attrs={'type':'date',
                                                                    'class': 'form-control'})

    class Meta(UserCreationForm.Meta):
        model = ConferenceGuest
        fields = ['username',
                  'first_name',
                  'last_name',
                  'email',
                  'birth_date',
                  'password1',
                  'password2']
```

Форма регистрации посещения
```python
class AttendanceRegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['form_author'].widget = forms.HiddenInput()
        self.fields['form_author'].required = False
    class Meta:
        model = ConferenceAttendance
        fields = ['conference',
                  'guest',
                  'role',
                  'form_author'
                  ]
        labels = {
            'conference': 'Choose your conference',
            'password': 'Choose the guest',
            'role': 'At the conference you are:',
        }
```

Форма добавления комментариев
```python
class CommentsRegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].widget = forms.HiddenInput()
        self.fields['user'].required = False

    class Meta:
        model = ConferenceComments
        fields = ['user',
                  'conference',
                  'text',
                  'type',
                  ]
        labels = {
            'conference': 'Choose your conference',
            'text': 'Type the comment',
            'type': 'How would you rate the conference from 1 to 10?',
        }
```

Форма для регистрации лекции
```python
class LecturesRegisterForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        given_at = cleaned_data.get('given_at')
        conference = self.instance.conference
        if given_at and (given_at < conference.date_begin or given_at > conference.date_end):
            raise forms.ValidationError('The lecture must be scheduled within the conference dates.')
        return cleaned_data

    class Meta:
        model = ConferenceLectures
        fields = ['lecturer',
                  'name',
                  'given_at',
                  ]
        labels = {
            'lecturer': 'Who will give the lecture?',
            'name': 'How is the lecture called?',
            'given_at': 'When will the lecture be given?',
        }
        widgets = {
            'given_at': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}
            ),
        }
```
