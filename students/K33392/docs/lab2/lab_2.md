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

# Модели

### Отель (Hotel)

- Модель `Hotel` представляет собой отель со следующими полями:
  - `name` (CharField): Название отеля (максимальная длина: 200 символов).
  - `owner` (CharField): Владелец отеля (максимальная длина: 100 символов).
  - `address` (TextField): Адрес отеля.
  - `description` (TextField): Описание отеля.
  - `room_types` (TextField): Описание доступных типов номеров.
  - `price` (DecimalField): Цена номеров в отеле (максимальное количество цифр: 10, количество десятичных знаков: 2).
  - `capacity` (PositiveIntegerField): Максимальная вместимость отеля.
  - `amenities` (TextField): Описание удобств в отеле.

```python
  from django.db import models

  class Hotel(models.Model):
      name = models.CharField(max_length=200)
      owner = models.CharField(max_length=100)
      address = models.TextField()
      description = models.TextField()
      room_types = models.TextField()
      price = models.DecimalField(max_digits=10, decimal_places=2)
      capacity = models.PositiveIntegerField()
      amenities = models.TextField()

      def __str__(self):
          return self.name
```

### Бронь (Reservation)

- Модель `Reservation` представляет собой бронирование, сделанное пользователем, со следующими полями:
  - `user` (ForeignKey к модели User): Пользователь, сделавший бронирование.
  - `hotel` (ForeignKey к модели Hotel): Отель, для которого сделано бронирование.
  - `check_in_date` (DateField): Дата заселения в отель.
  - `check_out_date` (DateField): Дата выселения из отеля.
  - `num_guests` (PositiveIntegerField): Количество гостей в бронировании.
  - `additional_notes` (TextField, необязательно): Дополнительные замечания или комментарии к бронированию.

```python
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    num_guests = models.PositiveIntegerField()
    additional_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Reservation for {self.user.username} at {self.hotel.name}'
```

### Отзыв (Review)

- Модель `Review` представляет собой отзыв пользователя о гостинице со следующими полями:
  - `user` (ForeignKey к модели User): Пользователь, написавший отзыв.
  - `hotel` (ForeignKey к модели Hotel): Гостиница, которую пользователь оценивает.
  - `check_in_date` (DateField, по умолчанию: 1970-01-01): Дата заселения пользователя.
  - `check_out_date` (DateField, по умолчанию: 1970-01-01): Дата выселения пользователя.
  - `review_text` (TextField): Текст отзыва.
  - `rating` (PositiveIntegerField, выбор с 1 по 10): Рейтинг, присвоенный пользователем.
  - `additional_comments` (TextField): Дополнительные комментарии или отзыв пользователя.
  - `created_at` (DateTimeField, автоматически создается): Временная метка создания отзыва.

```python
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    check_in_date = models.DateField(default=datetime(1970, 1, 1))
    check_out_date = models.DateField(default=datetime(1970, 1, 1))
    review_text = models.TextField()
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 11)])
    additional_comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user.username} for {self.hotel.name}'


```

### Профиль (Profile)

- Модель `Profile` представляет собой профиль пользователя с одним-к-одному отношением к модели User.

```python

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
```

# Представления

### hotel_list

- `hotel_list` - представление, которое отображает список отелей.
- Получает все отели из базы данных с помощью `Hotel.objects.all()`.
- Отправляет отели на страницу "hotel_list.html" для отображения.

```python

def hotel_list(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotel_list.html', {'hotels': hotels})

```

### hotel_detail

- `hotel_detail` - представление, которое отображает детали конкретного отеля.
- Получает объект отеля с помощью `Hotel.objects.get(id=hotel_id)`.
- Проверяет, есть ли у пользователя бронирование для данного отеля.
- Отправляет информацию об отеле и флаг `user_has_reservation` на страницу "hotel_detail.html" для отображения.

```python

def hotel_detail(request, hotel_id):
    hotel = Hotel.objects.get(id=hotel_id)
    user_has_reservation = False
    if request.user.is_authenticated:
        user_has_reservation = Reservation.objects.filter(user=request.user, hotel=hotel).exists()

    context = {
        'hotel': hotel,
        'user_has_reservation': user_has_reservation,
    }

    return render(request, 'hotel_detail.html', context)
```

### user_login

- `user_login` - представление для аутентификации пользователя.
- Проверяет отправленные данные формы и аутентифицирует пользователя.
- Перенаправляет аутентифицированных пользователей на страницу "hotel_list".

```python

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('hotel_list')
        else:
            pass
    return render(request, 'login.html')

```

### user_logout

- `user_logout` - представление для выхода пользователя из системы.
- Выполняет выход пользователя и перенаправляет на страницу "hotel_list".

```python

@login_required
def user_logout(request):
    logout(request)
    return redirect('hotel_list')

```

### register

- `register` - представление для регистрации новых пользователей.
- Проверяет отправленные данные формы, создает нового пользователя и выполняет вход для него.
- Перенаправляет на страницу "hotel_list" после успешной регистрации.

```python

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('hotel_list')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

```

### make_reservation

- `make_reservation` - представление для создания бронирования.
- Получает данные о бронировании из формы и сохраняет их в базе данных.
- Перенаправляет на страницу "reservation_confirmation" после успешного создания бронирования.

```python

@login_required
def make_reservation(request, hotel_id):
    hotel = Hotel.objects.get(id=hotel_id)

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.hotel = hotel
            reservation.save()
            return redirect('reservation_confirmation')
    else:
        form = ReservationForm()

    return render(request, 'make_reservation.html', {'form': form, 'hotel': hotel})

```

### reservation_confirmation

- `reservation_confirmation` - представление, подтверждающее успешное создание бронирования.

```python

@login_required
def reservation_confirmation(request):
    return render(request, 'reservation_confirmation.html')

```

### reservation_list

- `reservation_list` - представление, отображающее список бронирований пользователя.
- Получает бронирования, принадлежащие текущему пользователю, и отправляет их на страницу "reservation_list.html" для отображения.

### cancel_reservation

- `cancel_reservation` - представление для отмены бронирования.
- Позволяет пользователю отменить свое бронирование.
- Перенаправляет на страницу "reservation_list" после отмены бронирования.

### last_month_guests

- `last_month_guests` - представление, отображающее гостей, заселившихся в последний месяц.
- Получает бронирования, где дата заселения попадает в последний месяц, и отправляет их на страницу "last_month_guests.html" для отображения.

### leave_review

- `leave_review` - представление для создания отзыва о гостинице.
- Получает данные о отзыве из формы и сохраняет их в базе данных.
- Перенаправляет на страницу "hotel_detail" после успешного создания отзыва.

```python
@login_required
def leave_review(request, hotel_id):
    hotel = Hotel.objects.get(id=hotel_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.hotel = hotel

            reservation = Reservation.objects.filter(user=request.user, hotel=hotel).latest('check_in_date')

            review.check_in_date = reservation.check_in_date
            review.check_out_date = reservation.check_out_date

            review.save()
            return redirect('hotel_detail', hotel_id=hotel_id)
    else:
        form = ReviewForm()

    return render(request, 'leave_review.html', {'form': form, 'hotel': hotel})
```
