# Формы
Формы в Django — это классы, которые описывают данные, вводимые пользователем. Из них собираются формы на стороне frontend-а. Они хранятся в файле forms.py внутри приложения.

В рамках данной лабораторной работы структура этого файла следующая:
```python
from django.forms import ModelForm
from .models import Booking, Customer, Review
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BookingForm(ModelForm):
	class Meta:
		model = Booking
		fields = ['check_in_date', 'check_out_date']
		
class EditBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['check_in_date', 'check_out_date']
		
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'
		exclude = ['user']
            
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        exclude = ['booking']
```

Этот файл содержит различные формы для работы с моделями данных в Django:

* BookingForm: используется для создания бронирования (Booking) номеров отеля и содержит поля для даты заезда и выезда.

* EditBookingForm: предназначена для редактирования существующего бронирования и также содержит поля для изменения даты заезда и выезда.

* CreateUserForm: форма для регистрации новых пользователей (User) с использованием встроенной формы UserCreationForm, включающей поля для имени пользователя, электронной почты и пароля.

* CustomerForm: используется для создания или редактирования данных о клиентах (Customer) отеля, содержит все поля из модели Customer, за исключением поля пользователя (user).

* ReviewForm: форма для создания отзывов (Review) к номерам отеля, включает поля для рейтинга, комментария и даты создания.

Каждая форма связана с соответствующей моделью данных и определяет, какие поля будут отображаться и какие операции можно выполнять с данными.