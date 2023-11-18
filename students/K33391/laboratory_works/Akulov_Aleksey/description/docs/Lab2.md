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

### Модель базы данных

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


### Формы


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