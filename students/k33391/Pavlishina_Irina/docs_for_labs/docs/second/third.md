# Формы


###  Импорты

```
from django import forms
from .models import Passenger, Reservation, Comment, Seat
```

###  Форма регистрации

```
class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = ["username", "password", "first_name", "last_name", "email", "passport"]
```

###  Форма пассажира

```
class LoginForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = ["username", "password"]
```

###  Форма брони

```
class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ["seat"]
```

###  Форма отзыва

```
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["rating", "text"]

```