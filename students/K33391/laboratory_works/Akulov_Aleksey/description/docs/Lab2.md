# Отчет по лабораторной работе №2

Выполнил: Акулов Алексей, K33391

#### Цель работы:

Овладеть практическими навыками и умениями реализации web-серверов поработать с Django.


## Задание

Необходимо учитывать название отеля, владельца отеля, адрес, описание, типы
номеров, стоимость, вместимость, удобства.
Необходимо реализовать следующий функционал:
- Регистрация новых пользователей.
- Просмотр и резервирование номеров. Пользователь должен иметь
возможность редактирования и удаления своих резервирований.
- Написание отзывов к номерам. При добавлении комментариев, должны
сохраняться период проживания, текст комментария, рейтинг (1-10),
информация о комментаторе.
- Администратор должен иметь возможность заселить пользователя в отель и
выселить из отеля средствами Django-admin.
- В клиентской части должна формироваться таблица, отображающая
постояльцев отеля за последний месяц.


### Создание проекта
Для начала нам необходимо создать виртуальную среду для Python, установить Django и
создать проект
```
pip install django
django-admin starproject lab_2
```

После создания проекта нам необходимо добавить в данный проект приложение, которое мы будем разрабатывать
```
./manage.py startapp hotels
```

## Модель базы данных

Были созданы следующие таблицы: 

1. Посетители: сожержит информацию о постояльцах отелей
2. Отели: содержит информацию об отеле и его владельце
3. Уобства: нужны для подлючения в номерах
4. Тип комнаты: представляет собой тип комнаты, который есть в определенном отеле
5. Брони: представляет связь между постояльцем и типом комнаты
6. Обзор: представляет обзор постояльца на комнату, в котрой он проживал

после написания и изменения моделей нобходимо не забывать применять миграции

```
class Visitor(AbstractUser):
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    birth_date = models.DateTimeField(null=True, blank=True)
    passport = models.CharField(max_length=25, null=True)


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100)
    owner_contact = models.CharField(max_length=100)
    address = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Amenity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class RoomType(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField()
    amenities = models.ManyToManyField(Amenity,
                                       related_name='room_types', blank=True)

    def __str__(self):
        return f'{self.hotel}-{self.name}'


class Reservation(models.Model):
    user = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'Reservation {self.user} - {self.id}'


class Review(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
    stay_from = models.DateField()
    stay_to = models.DateField()
    author = models.ForeignKey(Visitor, on_delete=models.CASCADE)

```


## Формы

Необходимо создать формы для корректного отображения постояльца, отзыва и брони

```

class VisitorCreationForm(UserCreationForm):
    class Meta:
        model = Visitor
        fields = ('username', 'email', 'surname', 'name', 'passport',
                  'password1', 'password2')


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['room_type', 'start_date', 'end_date']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'stay_from', 'stay_to', 'comment', 'author']
        widgets = {
            'stay_from': forms.DateInput(attrs={'type': 'date'}),
            'stay_to': forms.DateInput(attrs={'type': 'date'}),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 10})
        }

```

## Создание view

Для реализации видов будем использвоать способ через функции
Необходимо реализовать все нужные нам виды:
1. Список отелей
2. Регистрация, использует форму для пользователя
3. Листр броней: перечисляет все брони человек. Используется форма брони, изначально происходит верификация пользователя
   - Создание новой брони
   - Редактивроание брони
   - Удаление брони
   - Написание отзыва
4. Также нужны админские виды для просмотра резерваций и просмотра всех постояльцев за последний месяц
5. Вид для отображения вступительной страницы

```


def hotel_list(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotel_list.html', {'hotels': hotels})


def register(request):
    if request.method == 'POST':
        form = VisitorCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('hotel_list')
    else:
        form = VisitorCreationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def reservation_list(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'reservation_list.html',
                  {'reservations': reservations})


@login_required
def reservation_create(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            return redirect('reservation_list')
    else:
        form = ReservationForm()
    return render(request, 'reservation_create.html', {'form': form})


@login_required
def reservation_edit(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id,
                                    user=request.user)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('reservation_list')
    else:
        form = ReservationForm(instance=reservation)

    return render(request, 'reservation_edit.html',
                  {'form': form, 'reservation': reservation})


@login_required
def reservation_delete(request, reservation_id):
    reservation = get_object_or_404(Reservation,
                                    pk=reservation_id, user=request.user)
    if request.method == 'POST':
        reservation.delete()
        return redirect('reservation_list')
    return render(request, 'reservation_delete.html',
                  {'reservation': reservation})


def is_admin(user):
    return user.is_authenticated and user.is_staff


@login_required
@user_passes_test(is_admin)
def admin_reservation_list(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    reservation = Reservation.objects.filter(user=user)
    return render(request, 'admin_reservations_list.html',
                  {'reservation': reservation, 'reserved_user': user})



@login_required
def review(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)

    if request.user != reservation.user:
        return redirect('reservation_list')

    review, created = Review.objects.get_or_create(
        reservation=reservation,
        defaults={
            'author': request.user,
            'rating': 10,
            'stay_from': reservation.start_date,
            'stay_to': reservation.end_date,
        }
    )

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            if created:
                review = form.save(commit=False)
                review.author = request.user
                review.save()
            else:
                form.save()
            return redirect('reservation_list')
    else:
        form = ReviewForm(instance=review)

    return render(request, 'review.html',
                  {'form': form, 'reservation': reservation})


def hotel_guests(request):
    today = datetime.now().date()
    first_day = today.replace(day=1)

    reservations_last_month = Reservation.objects.filter(
        start_date__gte=first_day)

    hotels_with_guests = {}
    for reservation in reservations_last_month:
        hotel_name = reservation.room_type.hotel.name
        if hotel_name not in hotels_with_guests:
            hotels_with_guests[hotel_name] = []
        hotels_with_guests[hotel_name].append(reservation)

    return render(request, 'hotel_guests.html',
                  {'hotels_with_guests': hotels_with_guests})


def welcome_page(request):
    return render(request, 'welcome.html')
```

## Ссылки

Нужно написать ссылки для всех созданых страниц и написать html реализациюю Нужно еще не забыть написать в настройках место для ссылок

```
urlpatterns = [

    path('register/', register, name='register'),

    path('hotels/', hotel_list, name='hotel_list'),

    path('reservations/', reservation_list, name='reservation_list'),

    path('reservations/edit/<int:reservation_id>/',
         reservation_edit, name='reservation_edit'),

    path('reservations/delete/<int:reservation_id>/',
         reservation_delete, name='reservation_delete'),

    path('reservation/create/', reservation_create, name='reservation_create'),

    path('login/', LoginView.as_view(template_name='login.html'),
         name='login'),

    path('reservations/<int:user_id>/',
         admin_reservation_list, name='admin_reservation_list'),

    path('reservations/<int:reservation_id>/review/', review, name='review'),

    path('hotel-guests/', hotel_guests, name='hotel_guests'),

    path('', welcome_page, name='welcome_page')

]
```