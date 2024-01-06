# Представления

В этом разделе представлены представления (views) Django для проекта "Табло авиаперелетов". Представления обрабатывают HTTP-запросы от клиентов и возвращают HTML-страницы или выполняют другие действия. Они выполняют ключевые функции в проекте.

## Главная страница (`home`)

Это представление отвечает за отображение главной страницы проекта. Оно использует шаблон "home.html" для отображения содержимого. Просто отображает главную страницу.

```python
def home(request):
    return render(request, 'home.html')
```

## Регистрация (`registration_view`)

Представление для обработки регистрации пользователей. Если запрос метода POST, оно обрабатывает данные, введенные пользователем, и создает нового пользователя. После успешной регистрации пользователь входит в систему и перенаправляется на страницу личного кабинета. Если запрос метода GET, представление просто отображает форму регистрации.

```python
def registration_view(request):
    if request.method == 'POST':
        # Обработка регистрации
    else:
        # Отображение формы регистрации
    return render(request, 'register.html', {'form': form})
```

## Вход в систему (`login_view`)

Представление для обработки входа пользователей. Если запрос метода POST, оно проверяет введенные данные пользователя и, при успешном входе, перенаправляет на страницу личного кабинета. Если запрос метода GET, представление отображает форму входа.

```python
def login_view(request):
    if request.method == 'POST':
        # Обработка входа
    else:
        # Отображение формы входа
    return render(request, 'login.html')
```

## Выход из системы (`logout_view`)

Представление для выхода пользователя из системы. Оно выполняет выход и перенаправляет на главную страницу.

```python
def logout_view(request):
    logout(request)
    return redirect('/')
```

## Личный кабинет (`personal_space_view`)

Представление для отображения личного кабинета пользователя. Требует аутентификации пользователя. Отображает информацию о пользователе и предоставляет доступ к другим функциям.

```python
@login_required
def personal_space_view(request):
    username = request.user.username
    return render(request, 'personal_space.html', {'username': username})
```

## Просмотр списка броней (`show_user_reservations`)

Представление для отображения списка броней пользователя. Требует аутентификации пользователя. Получает список броней, связанных с пользователем, и отображает их.

```python
@login_required
def show_user_reservations(request):
    user = request.user
    reservations = Reservation.objects.filter(user=user)
    return render(request, 'user_reservations.html', {'reservations': reservations})
```

## Редактирование брони (`edit_reservation`)

Представление для редактирования существующей брони. Получает данные о брони и обрабатывает их. Позволяет пользователю изменять информацию о брони.

```python
@login_required
def edit_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('user_reservations')
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'edit_reservation.html', {'form': form})
```

## Удаление брони (`delete_reservation`)

Представление для удаления существующей брони. Получает данные о брони и удаляет ее.

```python
@login_required
def delete_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    if request.method == 'POST':
        reservation.delete()
        return redirect('user_reservations')
    return render(request, 'delete_reservation.html', {'reservation': reservation})
```

## Пассажиры рейса (`flight_passengers`)

Представление для отображения списка пассажиров на конкретном рейсе. Получает данные о рейсе и связанных с ним бронях, а затем отображает список пассажиров.

```python
@login_required
def flight_passengers(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    reservations = Reservation.objects.filter(flight=flight)
    return render(request, 'flight_passengers.html', {'flight': flight, 'reservations': reservations})
```

## Создание отзыва (`create_review`)

Представление для создания отзыва о конкретном рейсе. Получает данные о рейсе и обрабатывает отправленный отзыв. Сохраняет отзыв, связывая его с рейсом и пользователем.

```python
@login_required
def create_review(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.flight = flight
            review.user = request.user
            review.date = timezone.now()  # Set the date field manually
            review.save()
            return redirect('flight_reviews', flight_id)
    else:
        form = ReviewForm()

    return render(request, 'create_review.html', {'form': form, 'flight': flight})
```

## Отзывы о рейсе (`flight_reviews`)

Представление для отображения списка отзывов о конкретном рейсе. Получает данные о рейсе и отображает список связанных с ним отзывов.

```python
def flight_reviews(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    reviews = Review.objects.filter(flight=flight)
    return render(request, 'show_flight_reviews.html', {'flight': flight, 'reviews': reviews})
```

## Список рейсов (`flights_list`)

Представление для отображения списка всех рейсов. Получает данные о всех рейсах и отображает их список.

```pythondef flights_list(request):
    # Отображение списка всех рейсов
def flights_list(request):
    flights = Flight.objects.all()
    return render(request, 'all_flights_list.html', {'flights': flights})
```

Эти представления обеспечивают основной функционал проекта "Табло авиаперелетов", позволяя пользователям регистрироваться, входить в систему, просматривать информацию о рейсах, бронировать билеты, писать отзывы и многое другое.
