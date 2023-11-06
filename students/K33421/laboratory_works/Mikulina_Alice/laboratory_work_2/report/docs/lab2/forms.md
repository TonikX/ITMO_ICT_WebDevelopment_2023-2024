# Forms

Форма регистрации

```
class RegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2',
                  'email', 'first_name', 'last_name', 'country',
                  'profile_picture', 'about_info']
```

Форма редактирования профиля

```
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'first_name', 'last_name', 'country',
                  'profile_picture', 'about_info']
```
Форма отзыва

```
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['reservation', 'rating', 'body']
        labels = {
            'reservation': 'reservation',
            'rating': 'rating',
            'body': 'body',
        }

    def __init__(self, *args, **kwargs):
        """Save the request with the form so it can be accessed in clean_*()"""
        self.request = kwargs.pop('request', None)
        super(ReviewForm, self).__init__(*args, **kwargs)

    def clean_name(self):
        """Make sure people don't use my name"""
        data = self.cleaned_data['name']
        if not self.request.user.is_authenticated and data.lower().strip() == 'samuel':
            raise ValidationError("Sorry, you cannot use this name.")
        return data
```
Форма резервирования

```
class ReservationForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['guest'].widget = forms.HiddenInput()
        self.fields['room'].widget = forms.HiddenInput()
        self.fields['guest'].required = False
        self.fields['room'].required = False


    def clean(self):
            cleaned_data = super().clean()
            start_date = cleaned_data.get('start_date')
            end_date = cleaned_data.get('end_date')
            
            room = self.instance.room  # Get the room for the reservation
            
            # Check if the room is available for the given dates
            if not room.available(start_date, end_date):
                raise ValidationError('The room is not available for the selected dates.')
            
            return cleaned_data
    
    class Meta:
        model = Reservation
        fields = ['room', 'guest', 'start_date', 'end_date']
        labels = {
            'room': 'room',
            'guest': 'guest',
            'start_date': 'start_date',
            'end_date': 'end_date',
        }
        widgets = {
            'start_date': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}
            ),
            'end_date': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}
            ),
        }
```