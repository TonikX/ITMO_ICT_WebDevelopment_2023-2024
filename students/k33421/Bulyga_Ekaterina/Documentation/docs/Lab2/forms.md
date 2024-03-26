<h1>Форма регистрации</h1>

<pre>
<code>
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    name = forms.CharField(label='', max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}))
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}), error_messages={'invalid': 'Неверный email'})

    class Meta:
        model = User
        fields = ('username', 'name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        self.error_messages['password_mismatch'] = 'Пароли не совпадают'
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Логин'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Пароль'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Подтвердите пароль'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"></span>'
</code>
</pre>