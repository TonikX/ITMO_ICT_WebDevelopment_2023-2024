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
