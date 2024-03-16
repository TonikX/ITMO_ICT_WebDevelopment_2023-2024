# Модели
Модели в Django — это классы, которые описывают структуру данных. Они хранятся в файле mode
ls.py внутри приложения. В рамках данной лабораторной работы структура этого файла следующая:
```python
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

class Hotel(models.Model):
    name = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    website = models.CharField(max_length=200, null=True)
    phone = PhoneNumberField()
    owner = models.CharField(max_length=200, null=True)
    rating = models.FloatField(
        validators=[
            MinValueValidator(1.0),
            MaxValueValidator(5.0),
        ],
        null=True
    )
    small_description = models.CharField(max_length=400, null=True)
    full_description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def calculate_rating(self):
        reviews = Review.objects.filter(booking__room__hotel=self)
        if reviews.exists():
            total_rating = sum(review.rating for review in reviews)
            average_rating = round(total_rating / reviews.count(), 1)
            self.rating = average_rating
        else:
            self.rating = 0.0

        self.save()

    def __str__(self):
        return self.name

class Room(models.Model):
    CATEGORY = (
        ('Basic', 'Basic'),
        ('Premium', 'Premium'),
        ('Deluxe', 'Deluxe'),
        ('Ultra Deluxe', 'Ultra Deluxe')
    )
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')
    category = models.CharField(max_length=200, choices=CATEGORY)
    price = models.FloatField()
    amenities = models.TextField()
    image = models.ImageField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.hotel.name} - {self.category} Room"

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True, blank=True)
    date_registered = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
    
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from datetime import timedelta

class Booking(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
        ('Checked In', 'Checked In'),
        ('Completed', 'Completed')
    )
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='reservations')
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    check_in_date = models.DateField()
    check_out_date = models.DateField()

    @property
    def price(self):
        if self.check_in_date and self.check_out_date:
            duration = (self.check_out_date - self.check_in_date).days
            if duration < 1:
                return self.room.price
            else:
                return self.room.price * duration
        return 0
    
    @property
    def days_spent(self):
        if self.status == 'Completed':
            return (self.check_out_date - self.check_in_date).days
        return 0

    def save(self, *args, **kwargs):
        if not self.price:
            self.price = self.room.price
        super(Booking, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.name} - {self.room.hotel.name} - {self.room.category} booking"


    
class Review(models.Model):
    booking = models.OneToOneField(Booking, null=True, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def save(self, *args, **kwargs):
        super(Review, self).save(*args, **kwargs)
        self.booking.room.hotel.calculate_rating()

    def __str__(self):
        return f"{self.booking.user.name} - {self.booking.room} review"


```

Этот файл содержит модели данных для веб-приложения на Django:

* Hotel (Отель): содержит информацию о названии, адресе, веб-сайте, телефоне, владельце, рейтинге, описании и изображении отеля.

* Room (Номер): хранит данные о номерах в отеле, включая категорию, цену, удобства и изображение.

* Customer (Пользователь): связан с моделью User из Django и содержит информацию о клиентах, такую как имя, электронная почта и телефон.

* Booking (Бронирование): представляет информацию о бронированиях номеров клиентами, включая статус, даты заезда и выезда, цену и длительность пребывания.

* Review (Отзыв): используется для оценки и комментирования номеров отеля клиентами, содержит рейтинг, комментарий и дату создания.

Эти модели содержат различные поля для хранения данных и методы для выполнения операций с ними, такие как вычисление среднего рейтинга отеля или цены бронирования.