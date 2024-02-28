# Формы

### Форма регистрации (RegistrationForm)

- `RegistrationForm` представляет собой форму для регистрации пользователей с использованием `UserCreationForm` из Django. Форма включает следующие поля:
  - `username` (CharField): Имя пользователя.
  - `email` (EmailField): Адрес электронной почты пользователя.
  - `password1` (CharField): Пароль.
  - `password2` (CharField): Подтверждение пароля.

```python

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=100, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

```

### Форма бронирования (ReservationForm)

- `ReservationForm` представляет собой форму для создания бронирования с использованием модели `Reservation`. Форма включает следующие поля:
  - `check_in_date` (DateField): Дата заселения.
  - `check_out_date` (DateField): Дата выселения.
  - `num_guests` (PositiveIntegerField): Количество гостей.
  - `additional_notes` (TextField, необязательно): Дополнительные замечания или комментарии к бронированию.

```python

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['check_in_date', 'check_out_date', 'num_guests', 'additional_notes']

```

### Форма отзыва (ReviewForm)

- `ReviewForm` представляет собой форму для создания отзыва с использованием модели `Review`. Форма включает следующие поля:
  - `review_text` (TextField): Текст отзыва.
  - `rating` (PositiveIntegerField): Рейтинг отзыва.

```python
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review_text', 'rating']
```
