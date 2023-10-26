# Создание базы данных

>Табло отображения информации об авиаперелетах.
Хранится информация о номере рейса, авиакомпании, отлете, прилете, типе
(прилет, отлет), номере гейта.
Необходимо реализовать следующий функционал:
<br/>1)Регистрация новых пользователей.
<br/>2)Просмотр и резервирование мест на рейсах. Пользователь должен иметь
возможность редактирования и удаления своих резервирований.
<br/>3)Администратор должен иметь возможность зарегистрировать на рейс
пассажира и вписать в систему номер его билета средствами Django-admin.
<br/>4)В клиентской части должна формироваться таблица, отображающая всех
пассажиров рейса.
<br/>5)Написание отзывов к рейсам. При добавлении комментариев, должны
сохраняться дата рейса, текст комментария, рейтинг (1-10), информация о
комментаторе.

**Было создано 6 таблиц - 5 основных для функционала и еще одна для комментариев**


**Traveler - пользователь**

```

class Traveler(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(null=True)
    passport = models.CharField(max_length=30)
    flights = models.ManyToManyField('Flight', through='Ticket')
    seats = models.ManyToManyField('Seat', through='Ticket')

```
**Ticket - билет (ассоциативная сущность между пользователем, местом и рейсом)**
</br>Дополнительное поле - наличие багажа. 
В дальнейшем при редактировании бронирования можно будет 
изменить только это поле, для изменения места нужно удалить билет и купить новый.

```

class Ticket(models.Model):
    traveler_id = models.ForeignKey('Traveler', on_delete=models.CASCADE)
    flight_id = models.ForeignKey('Flight', on_delete=models.CASCADE)
    seat_id = models.ForeignKey('Seat', on_delete=models.CASCADE)
    baggage = models.BooleanField(default=False)
    
```
**Flight - рейс**
</br>На рейсе используется самолет - на один рейс один самолет, но на один самолет - много рейсов.
</br> Рейс отображается как точка отпраления и точка посадки.
```

class Flight(models.Model):
    airline = models.CharField(max_length=30)
    departure_site = models.CharField(max_length=50)
    landing_site = models.CharField(max_length=50)
    departure_time = models.DateTimeField()
    landing_time = models.DateTimeField()
    gate = models.CharField(max_length=10)
    plane_id = models.ForeignKey('Plane', on_delete=models.CASCADE)
    travelers = models.ManyToManyField('Traveler', through='Ticket')
    seats = models.ManyToManyField('Seat', through='Ticket')

    def __str__(self):
        return self.departure_site + '-' + self.landing_site# + '(' + self.departure_time + '-' + self.landing_time + ')'

```
**Seat - место**
</br>Место привязано не к рейсу, а к самолету. 
Соответственно в зависимости от самолета в рейсе определяется количество мест.
Статуса бронирования у места нет по этой причине - занятые места вычисляются по другому, см. views.
```

class Seat(models.Model):
    name = models.CharField(max_length=10, primary_key=True)
    category = models.CharField(max_length=20)
    cost = models.IntegerField()
    plane_id = models.ForeignKey('Plane', on_delete=models.CASCADE)
    flights = models.ManyToManyField('Flight', through='Ticket')
    travelers = models.ManyToManyField('Traveler', through='Ticket')

    def __str__(self):
        return self.name
        
```
**Plane - самолет**
</br> Так как дополнительно условий касательно самолета не было - были введены всего два поля: количество мест и название
```

class Plane(models.Model):
    name = models.CharField(max_length=50)
    seats_number = models.IntegerField()

    def __str__(self):
        return self.name
        
```
**Comment - комментарии пользователя к рейсам**
</br> Комментарии оставляют пользователи для конкретного рейса и выставляют рейтинг
```

class Comment(models.Model):
    flight = models.ForeignKey('Flight', related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey('Traveler', on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(
         validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    date_added = models.DateTimeField(auto_now_add=True)
    date_flight = models.DateTimeField()
    
```