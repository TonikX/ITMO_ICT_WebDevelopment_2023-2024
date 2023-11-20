#forms.py

В этом файле определены различные формы, каждая из которых предназначена для работы с соответствующей моделью данных. 

    ReservationForm - форма для бронирования тура.
    SoldTourForm - форма для продажи тура.
    ReviewForm - форма для написания отзыва.
    RegistrationForm - форма для регистрации пользователя.

Эти формы позволяют собирать данные от пользователей через веб-интерфейс и взаимодействовать с соответствующими моделями данных в приложении Django.

```python
from django import forms
from .models import Reservation, Review, SoldTour
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ReservationForm(forms.ModelForm):
    """
    Форма для бронирования тура.
    """
    class Meta:
        model = Reservation
        fields = ['tour', 'is_confirmed']

class SoldTourForm(forms.ModelForm):
    """
    Форма для продажи тура.
    """
    class Meta:
        model = SoldTour
        fields = []

class ReviewForm(forms.ModelForm):
    """
    Форма для написания отзыва.
    """
    class Meta:
        model = Review
        fields = ['text', 'rating']

class RegistrationForm(UserCreationForm):
    """
    Форма для регистрации пользователя.
    """
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class ReservationForm(forms.ModelForm):
    """
    Дополнительная форма для бронирования.
    """
    class Meta:
        model = Reservation
        fields = []

class ReviewForm(forms.ModelForm):
    """
    Дополнительная форма для написания отзыва.
    """
    class Meta:
        model = Review
        fields = ['text', 'rating']
 
```