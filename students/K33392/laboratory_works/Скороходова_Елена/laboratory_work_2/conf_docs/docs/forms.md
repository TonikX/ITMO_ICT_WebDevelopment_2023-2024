#Формы
Используются для взаимодействия с данными, введенными или выбранными пользователями в HTML-формах.

##Форма регистрации пользователя
    class UserRegistrationForm(UserCreationForm):
        class Meta:
            model = User
            fields = ['username', 'first_name', 'last_name', 'email']

##Форма оставления отзыва
    class ReviewForm(forms.ModelForm):
        class Meta:
            model = Review
            fields = ['text', 'rating']
    
        def __init__(self, *args, **kwargs):
            super(ReviewForm, self).__init__(*args, **kwargs)

##Форма регистрации автора на конференцию
    class RegistrationForm(forms.ModelForm):
        class Meta:
            model = Registration
            fields = ['topic']
    
        def __init__(self, *args, **kwargs):
            user = kwargs.pop('user', None)
            super(RegistrationForm, self).__init__(*args, **kwargs)
    
            if user:
                self.fields['user'] = forms.ModelChoiceField(
                    queryset=user,
                    initial=user,
                    widget=forms.HiddenInput()
                )
